from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=Profile)
def update_notification_settings(sender, instance, **kwargs):
    if instance.receive_notifications == 'Do not send':
        instance.new_modules_notifications = 'Do not send'
        instance.quiz_results_notifications = 'Do not send'
        instance.discussion_notifications = 'Do not send'
        instance.new_resources_notifications = 'Do not send'