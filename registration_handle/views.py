from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from modules.models import Language

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
    learning_paths = {
        "Beginner": "You don't know the language that well and wish to get better at it.",
        "Skilled": "You know your stuff, but still need some help (trust us, you will get it here).:)",
        "Advanced": "You know the language, you 'd like to learn, really well! "
                    "But you still want to grow and learn more."
    }
    return render(request, 'learning_path_choice.html', {'languages': languages, 'learning_paths': learning_paths})
