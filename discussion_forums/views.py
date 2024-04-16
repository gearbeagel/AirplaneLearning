import os
import re
from datetime import datetime

from azure.storage.blob import BlobServiceClient
from django.contrib.auth.models import User
from django.contrib.humanize.templatetags import humanize
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from discussion_forums.models import Topic, Comment, CommentDeletionEvent
from modules.models import Module, Lesson


def main_forum_page(request):
    modules_for_topics = Module.objects.filter(language=request.user.profile.chosen_language)
    lessons_for_topics = Lesson.objects.filter(module__in=modules_for_topics)
    topics_for_lessons = Topic.objects.filter(subject__in=lessons_for_topics)
    all_topics = topics_for_lessons.order_by('-created_at')
    is_admin = request.user.is_superuser
    return render(request, "main_forum_page.html", {'all_topics': all_topics, 'is_admin': is_admin})

def topic_page(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    is_admin = True if request.user.is_superuser else False

    all_comments = Comment.objects.filter(topic_id=topic_id).order_by("-created_at")

    for comment in all_comments:
        comment.humanized_created_at = humanize.naturaltime(comment.created_at)

    profile_pictures = {}

    for comment in all_comments:
        user_profile = comment.created_by
        profile_pictures[user_profile.username] = get_profile_pic_url(user_profile)

    if request.method == 'POST':
        comment_text = request.POST.get('comment_text')
        if comment_text:
            if len(comment_text) <= 500:
                comment = Comment.objects.create(
                    message=comment_text,
                    topic=topic,
                    created_by=request.user.profile,
                    created_at=datetime.now()
                )
                comment.save()
                send_reply_notification_email(comment, comment_text)
                return redirect('topic_page', topic_id=topic_id)
            else:
                message = 'Your comment is too long! Make sure it is less than 500 symbols.'
                return render(request, 'topic_page.html',
                              {'topic': topic, 'all_comments': all_comments,
                               'profile_pictures': profile_pictures, 'message': message, 'is_admin': is_admin,
                               'request': request})
        else:
            message = 'Comment cannot be empty.'
            return render(request, 'topic_page.html',
                          {'topic': topic, 'all_comments': all_comments,
                           'profile_pictures': profile_pictures, 'message': message, 'is_admin': is_admin,
                           'request': request})
    return render(request, 'topic_page.html',
                  {'topic': topic, 'all_comments': all_comments,
                   'profile_pictures': profile_pictures, 'is_admin': is_admin, 'request': request})


def send_reply_notification_email(comment, comment_text):
    mentioned_usernames = re.findall(r'@(\w+)', comment_text)
    for username in mentioned_usernames:
        try:
            user = User.objects.get(username=username)
            if user.profile.receive_notifications == "Send":
                recipient_email = user.email
                subject = 'You have been mentioned in a comment'
                context = {'user': user, 'comment': comment}
                html_message = render_to_string('email_mention_notification.html', context)
                plain_message = strip_tags(html_message)
                send_mail(subject, plain_message, None, [recipient_email], html_message=html_message)
        except User.DoesNotExist:
            pass


def get_profile_pic_url(student):
    azure_storage_connection_string = os.getenv("connection_str")
    container_name = "pfpcontainer"
    blob_service_client = BlobServiceClient.from_connection_string(azure_storage_connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=student.profile_pic_url)
    profile_pic_url = blob_client.url
    return profile_pic_url


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        if request.user == comment.created_by.user or request.user.is_superuser:
            com_event = CommentDeletionEvent.objects.create(comment=comment, deleted_by=request.user)
            com_event.save()
            comment.delete()
            return redirect('topic_page', topic_id=comment.topic_id)
        else:
            pass
    return redirect('topic_page', topic_id=comment.topic_id)
