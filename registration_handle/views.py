from django.contrib.auth.models import User
from django.shortcuts import render


def home(request):
    return render(request, "homepage.html")


def register(request):
    if request.user.is_authenticated:
        user, created = User.objects.get_or_create(user=request.user)
        user.save()
    return render(request, "register.html")
