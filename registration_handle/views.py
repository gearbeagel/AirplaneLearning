import random
import secrets
import string

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse

from profile_page.models import Profile


def home(request):
    return render(request, "homepage.html")


def register(request):
    return render(request, "register.html")
