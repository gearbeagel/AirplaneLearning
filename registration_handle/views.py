from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def home(request):
    return render(request, "homepage.html")


def register(request):
    return render(request, "register.html")


def callback_view(request):
    return redirect('/langs')
