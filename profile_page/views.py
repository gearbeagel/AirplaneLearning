from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

from django.contrib.auth.models import User
from .models import LeeriApprentices


def profile_page(request):
    user = User.objects.get(username=request.user.username)
    email = user.email
    username = extract_username_from_email(email)

    student, created = LeeriApprentices.objects.get_or_create(username=username)

    student.username = username
    student.save()

    return render(request, 'profile_page.html', {'username': username})


def extract_username_from_email(email):
    parts = email.split('@')
    username = parts[0]
    return username
