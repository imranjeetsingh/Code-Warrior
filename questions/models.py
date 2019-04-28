import os

from django.db import models
from django.urls import reverse


def upload_question_image_location(instance, filename):
    file, ext = os.path.splitext(filename)
    location = 'questions/{code}{extension}'.format(code=instance.code, extension=ext)
    return location


class QuestionManager(models.Manager):

    def get_by_code(self, code):
        qs = self.get_queryset().filter(code=code)
        if qs.count() == 1:
            return qs.first()
        return None


class Question(models.Model):
    code = models.CharField(unique=True, max_length=10)
    title = models.CharField(unique=True, max_length=120)
    description = models.ImageField(upload_to=upload_question_image_location)
    time_limit = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = QuestionManager()

    def __str__(self):
        return self.code

    def get_absolute_url(self):
        return reverse('question:detail', kwargs={'code': self.code})

    def get_submit_url(self):
        return reverse('grader:submit', kwargs={'code': self.code})


def upload_test_case_file_location(instance, filename):
    location = 'test_cases/{code}/inputs/'.format(code=instance.question.code)
    return location + filename


class TestCaseQuerySet(models.query.QuerySet):

    def get_by_question(self, question_code):
        return self.filter(question__code=question_code)


class TestCaseManager(models.Manager):

    def get_queryset(self):
        return TestCaseQuerySet(self.model, using=self._db)

    def get_by_question(self, question_code):
        return self.get_queryset().get_by_question(question_code)


class TestCase(models.Model):
    question = models.ForeignKey(Question)
    file = models.FileField(upload_to=upload_test_case_file_location)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = TestCaseManager()

    class Meta:
        ordering = ['file']

    def __str__(self):
        return self.question.code + ' - ' + self.file.name.split('/')[-1]

    @property
    def filename(self):
        """ Returns the name of the file without the preceding path """
        return self.file.name.split('/')[-1]


def upload_expected_output_file_location(instance, filename):
    location = 'test_cases/{code}/outputs/'.format(code=instance.question.code)
    return location + filename


class ExpectedOutputQuerySet(models.query.QuerySet):

    def get_by_question(self, question_code):
        return self.filter(question__code=question_code)

    def get_by_question_test_case(self, question_code, test_case):
        return self.get_by_question(question_code).filter(test_case=test_case)


class ExpectedOutputManager(models.Manager):

    def get_queryset(self):
        return ExpectedOutputQuerySet(self.model, using=self._db)

    def get_by_question(self, question_code):
        return self.get_queryset().get_by_question(question_code)

    def get_by_question_test_case(self, question_code, test_case):
        return self.get_queryset().get_by_question_test_case(question_code, test_case)


class ExpectedOutput(models.Model):
    question = models.ForeignKey(Question)
    test_case = models.ForeignKey(TestCase)
    file = models.FileField(upload_to=upload_expected_output_file_location)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ExpectedOutputManager()

    class Meta:
        ordering = ['file']

    def __str__(self):
        return self.question.code + ' - ' + self.file.name.split('/')[-1] + ' - ' + self.test_case.file.name.split('/')[-1]

    @property
    def filename(self):
        """ Returns the name of the file without the preceding path """
        return self.file.name.split('/')[-1]
