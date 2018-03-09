from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import authenticate, login, get_user_model
from django.views.generic import DetailView, FormView, CreateView

from .forms import LoginForm, RegisterForm


User = get_user_model()


class ProfileView(DetailView):
    template_name = 'accounts/profile.html'

    def get_object(self, *args, **kwargs):
        request = self.request
        username = self.kwargs.get('username')
        instance = User.objects.filter(username=username).first()
        if instance is None:
            raise Http404('User not found')
        return instance


def leaderboard_view(request):
    qs = User.objects.all()
    return render(request, 'accounts/leaderboard.html', {'object_list': qs})


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = '/'
    default_url = '/'

    def get_form_kwargs(self):
        kwargs = super(LoginView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


# def login_page(request):
#     if request.user.is_authenticated:
#         return redirect('home')

#     form = LoginForm(request.POST or None)
#     context = {
#         'form': form
#     }
#     if form.is_valid():
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             # TODO: Replace this with proper error
#             raise Http404
#     return render(request, 'accounts/login.html', context)


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/login/'


# def register_page(request):
#     if request.user.is_authenticated:
#         return redirect('home')

#     form = RegisterForm(request.POST or None)
#     context = {
#         'form': form
#     }
#     if form.is_valid():
#         form.save()
#         return redirect('login')
#     return render(request, 'accounts/register.html', context)
