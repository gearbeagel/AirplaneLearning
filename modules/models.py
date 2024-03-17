from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Language(models.Model):
    name = models.CharField(max_length=100)
    joke = models.TextField()

    def __str__(self):
        return self.name


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    module = models.ForeignKey('Module', on_delete=models.CASCADE, default="1")
    description = models.TextField()
    difficulty_level = models.CharField(
        max_length=20,
        choices=[
            ('easy', _('Easy')),
            ('medium', _('Medium')),
            ('hard', _('Hard')),
        ],
        default='easy'
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('not_started', _('Not Started')),
            ('in_progress', _('In Progress')),
            ('completed', _('Completed')),
        ],
        default='not_started',
    )

    sections = models.ManyToManyField('Section', related_name='lessons')

    def __str__(self):
        return self.title


class Quiz(models.Model):
    title = models.CharField(max_length=100)
    module = models.ForeignKey('Module', on_delete=models.CASCADE, default="1")
    description = models.TextField()
    difficulty_level = models.CharField(
        max_length=20,
        choices=[
            ('easy', _('Easy')),
            ('medium', _('Medium')),
            ('hard', _('Hard')),
        ],
        default='easy'
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('not_started', _('Not Started')),
            ('in_progress', _('In Progress')),
            ('completed', _('Completed')),
        ],
        default='not_started',
    )

    questions = models.ManyToManyField('Question', related_name='quizzes')

    def __str__(self):
        return self.title


class Module(models.Model):
    title = models.CharField(max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Section(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    contents = models.TextField()

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.CharField(max_length=15, choices=[("Y", "Correct"), ("N", "Incorrect")], default="Incorrect")

    def __str__(self):
        return self.text
