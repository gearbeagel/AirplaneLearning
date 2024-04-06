from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.db.models.signals import post_save
from django.dispatch import receiver

from profile_page.models import Profile
from .models import Lesson
from .user_progress_models import QuizStatus


@receiver(post_save, sender=Lesson)
def send_lesson_notification(sender, instance, created, **kwargs):
    if created:
        subject = "New Lesson Added"
        message = render_to_string('email_new_lesson.html', {'lesson': instance})

        # Filter users who study the language of the new lesson
        users_to_notify = Profile.objects.filter(chosen_language_id=instance.language_id)
        recipient_list = [user.user.email for user in users_to_notify]

        send_mail(subject, message, None, recipient_list)