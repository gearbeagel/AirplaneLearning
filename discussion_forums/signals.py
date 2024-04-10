from django.core.mail import send_mail
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from discussion_forums.models import Comment


@receiver(post_delete, sender=Comment)
def send_comment_deletion_notification(sender, instance, **kwargs):
    subject = "Your comment... was..."
    html_message = render_to_string('email_comment_deletion.html', {'comment': instance})
    plain_message = strip_tags(html_message)

    user_to_notify = instance.created_by.email

    send_mail(subject, plain_message, None, [user_to_notify], html_message=html_message)