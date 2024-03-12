from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
"""from profile_page.models import User"""


def home(request):
    return render(request, "homepage.html")


def register(request):
   return render(request, "register.html")


def callback_view(request):
    return redirect('langs')
