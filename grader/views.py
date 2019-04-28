from datetime import datetime
from datetime import timedelta

from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth import get_user_model

from .forms import SolutionForm
from .models import Solution
from questions.models import Question
from grader.util import start_time

User = get_user_model()


@login_required
def submit_solution(request, code):
    if request.method == 'POST':
        current_time = datetime.now()
        future = start_time+timedelta(hours=100000)
        if current_time > future:
            data = User.objects.all()
            username = request.user.username
            return render(request, 'accounts/leaderboard.html', {
                'object_list': data, 'msg': 'Contest has ended', 'username': username
            })
        form = SolutionForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.question = Question.objects.get_by_code(code)
            instance.user = request.user
            instance.language = request.POST.get('language')
            instance.save()
            form.save()
            return redirect(reverse('grader:grade', kwargs={'code': code, 'pk': instance.pk}))
    else:
        form = SolutionForm()
    language_list = ['c', 'cpp', 'py2', 'py3']
    return render(request, 'grader/user_submission.html', {'form': form, 'language_list': language_list})


@login_required
def check_solution(request, code, pk):
    qs = Solution.objects.get_by_user_question(request.user.username, code)
    submission = qs.filter(pk=pk).first()
    if submission is None:
        raise Http404

    if submission.result is None:
        # run submission
        submission.evaluate()

        if submission.result == 'ac' or submission.result == 'pc':
            previous_max_submission = qs.exclude(pk=submission.id).first()
            if previous_max_submission is not None:
                score_diff = submission.score - previous_max_submission.score
                if score_diff > 0:
                    time_diff_up = (submission.timestamp-previous_max_submission.timestamp).total_seconds()
                    submission.user.increment_score(score_diff)
                    submission.user.increment_time(time_diff_up)
            else:
                time_diff = (datetime.now() - start_time).total_seconds()
                submission.user.increment_score(submission.score)
                submission.user.increment_time(time_diff)

    return render(request, 'grader/result.html', {
        'result': submission.result,
        'score': submission.score
    })


class PreviousSubmission(ListView):
    template_name = 'grader/previous_submission.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        code = self.kwargs.get('code')
        return Solution.objects.get_by_user_question(request.user.username, code)
