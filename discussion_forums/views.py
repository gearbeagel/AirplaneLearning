import os

from azure.storage.blob import BlobServiceClient
from django.shortcuts import render, get_object_or_404, redirect

from discussion_forums.forms import TopicForm
from discussion_forums.models import Topic, Post
from modules.models import Lesson
from profile_page.models import Profile


def main_forum_page(request):
    all_topics = Topic.objects.order_by('-created_at')
    is_admin = True if request.user.is_superuser else False
    return render(request, "main_forum_page.html", {'all_topics': all_topics, 'is_admin': is_admin})


def add_topic(request):
    student = Profile.objects.get(user=request.user)
    all_subjects = Lesson.objects.all()
    profile_pic_url = student.profile_pic_url
    azure_storage_connection_string = os.getenv("connection_str")
    container_name = "pfpcontainer"
    blob_service_client = BlobServiceClient.from_connection_string(azure_storage_connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=profile_pic_url)

    profile_pic_url = blob_client.url
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.starter = student
            topic.save()
            return redirect('main_forum_page')
        else:
            print(form.errors)
    else:
        form = TopicForm()
    return render(request, 'add_topic.html', {'form': form, 'all_subjects': all_subjects, 'student': student,
                                              'profile_pic_url': profile_pic_url})

def topic_page(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    all_posts = Post.objects.filter(topic_id=topic_id)

    return render(request, 'topic_page.html', {'topic': topic, 'all_posts': all_posts})

