from django.core.mail import send_mail
from django.db.models.signals import post_delete, pre_delete
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from discussion_forums.models import Comment, CommentDeletionEvent


@receiver(pre_delete, sender=Comment)
def send_comment_deletion_notification(sender, instance, **kwargs):
    try:
        deletion_event = instance.commentdeletionevent_set
    except CommentDeletionEvent.DoesNotExist:
        return
    if instance.created_by.receive_notifications == "Send":
        if deletion_event.deleted_by.is_superuser:
            subject = "Your comment... was..."
            html_message = render_to_string('email_comment_deletion.html', {'comment': instance})
            plain_message = strip_tags(html_message)

            user_to_notify = instance.created_by.email

            send_mail(subject, plain_message, None, [user_to_notify], html_message=html_message)
