from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request, "homepage.html")


def register(request):
    return render(request, "register.html")


def callback_view(request):
    return redirect('profile')