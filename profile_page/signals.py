from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from modules.models import Lesson, Quiz
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        lessons = Lesson.objects.all()
        quizzes = Quiz.objects.all()
        for lesson in lessons:
            lesson.status = "Not Started"
            lesson.save()
        for quiz in quizzes:
            quiz.status = "Not Started"
            quiz.save()
