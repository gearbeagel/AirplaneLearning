from django.shortcuts import render, get_object_or_404, redirect

from discussion_forums.forms import TopicForm
from discussion_forums.models import Topic, Post
from modules.models import Lesson
from profile_page.models import Profile


def main_forum_page(request):
    all_topics = Topic.objects.order_by('-created_at')
    return render(request, "main_forum_page.html", {'all_topics': all_topics})


def forum_page_with_topics(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    all_posts = Post.objects.filter(topic=topic).order_by('-created_at')
    return render(request, "topic_page_with_forums.html", {'topic': topic, 'all_posts': all_posts})


def add_topic(request):
    student = Profile.objects.get(user=request.user)
    all_subjects = Lesson.objects.all()
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.starter = student
            topic.save()
            return redirect('main_forum_page')
    else:
        form = TopicForm()
    return render(request, 'add_topic.html', {'form': form, 'all_subjects': all_subjects, 'student': student})
