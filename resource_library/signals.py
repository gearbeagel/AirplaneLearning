from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.template.loader import render_to_string
from django.dispatch import receiver
from django.utils.html import strip_tags

from .models import Resource
from profile_page.models import Profile


@receiver(post_save, sender=Resource)
def send_module_notification(sender, instance, created, **kwargs):
    if created:
        subject = "New Resource Added"
        html_message = render_to_string('email_new_resource.html', {'resource': instance})
        plain_message = strip_tags(html_message)

        users_to_notify = Profile.objects.filter(chosen_language_id=instance.related_lesson.module.language.id, new_resources_notifications="Send")
        recipient_list = [user.user.email for user in users_to_notify]

        send_mail(subject, plain_message, None, recipient_list, html_message=html_message)
