import secrets
import string

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from profile_page.models import LeeriApprentices


def generate_random_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for i in range(length))


def home(request):
    return render(request, "homepage.html")


def register(request):
    return render(request, "register.html")


def callback_view(request):
    return redirect('/profile')


@login_required
def create_username(request):
    return render(request, 'create_username.html')


@login_required
def submit_username(request):
    if request.method == 'POST':
        print("Received POST request for submitting username")
        username = request.POST.get('username')
        email = request.user.email
        print("Received username:", username)
        print("User email:", email)

        if username:
            if not LeeriApprentices.objects.filter(username=username).exists():
                user = LeeriApprentices.objects.create_user(
                    username=username,
                    email=email,
                    password=make_password(generate_random_password()),
                    progress=0,
                )
                user.save()
                print("User created successfully")
                return redirect('/profile')
            else:
                print("Username is already taken")
                return render(request, 'create_username.html', {'error': 'Username is already taken'})
        else:
            print("No username provided")
            return render(request, 'create_username.html', {'error': 'Please enter a username'})
    else:
        print("GET request received for submit_username")
        return redirect('/create_username/')
