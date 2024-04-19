from django.core.mail import send_mail
from django.db.models.signals import post_delete, pre_delete, post_save, pre_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from discussion_forums.models import Comment, CommentDeletionEvent, Topic
from discussion_forums.utils import load_profanity_words, contains_profanity
from modules.models import Lesson


@receiver(post_delete, sender=Comment)
def send_comment_deletion_notification(sender, instance, **kwargs):
    if instance.created_by.discussion_notifications == "Send":
        subject = "Your comment... was..."
        html_message = render_to_string('email_comment_deletion.html', {'comment': instance})
        plain_message = strip_tags(html_message)
        user_to_notify = instance.created_by.email

        send_mail(subject, plain_message, None, [user_to_notify], html_message=html_message)


@receiver(post_save, sender=Lesson)
def create_discussion_topic(sender, instance, created, **kwargs):
    if created:
        content = f"Here, you will discuss your experience on learning {instance.title}"
        Topic.objects.create(
            title=instance.title,
            subject=instance,
            description=content,
        )