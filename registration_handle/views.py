from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from modules.models import Language
from profile_page.models import LearningPath


def home(request):
    return render(request, "homepage.html")


def register(request):
    if request.user.is_authenticated:
        user, created = User.objects.get_or_create(user=request.user)
        user.save()
    return render(request, "register.html")


def about(request):
    return render(request, "about.html")


def learning_path_selection(request):
    languages = Language.objects.all()
    learning_paths = LearningPath.objects.all()
    return render(request, 'learning_path_choice.html', {'languages': languages, 'learning_paths': learning_paths})
