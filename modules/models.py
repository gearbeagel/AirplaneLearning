from django.db import models
from django.utils.translation import gettext_lazy as _


class Language(models.Model):
    name = models.CharField(max_length=100)
    joke = models.TextField()

    def __str__(self):
        return self.name


class Module(models.Model):
    title = models.CharField(max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    lessons = models.ManyToManyField('Lesson', related_name='modules')
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, default="1")
    description = models.TextField()
    difficulty_level = models.CharField(
        max_length=20,
        choices=[
            ('easy', _('Easy')),
            ('medium', _('Medium')),
            ('hard', _('Hard')),
        ],
        default='medium'
    )
    STATUS_CHOICES = [
        ('not_started', _('Not Started')),
        ('in_progress', _('In Progress')),
        ('completed', _('Completed')),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='not_started',
    )

    sections = models.ManyToManyField('Section', related_name='sections')

    def __str__(self):
        return self.title


class Section(models.Model):
    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    contents = models.TextField()
