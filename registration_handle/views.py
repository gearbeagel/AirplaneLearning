import secrets
import string

from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import MyForm
from profile_page.models import LeeriApprentices


def generate_random_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for i in range(length))


def home(request):
    return render(request, "homepage.html")


def register(request):
    return render(request, "register.html")


def login(request):
    return redirect(reverse('profile'))


def callback_view(request):
    if request.user.is_authenticated:
        if request.user.socialaccount_set.filter(provider='google').exists():
            email = request.user.email
            default_username = 'userino'
            user = LeeriApprentices.objects.create_user(
                username=default_username,
                email=email,
                password=make_password(generate_random_password()),
                progress=0,
            )
            print("User created successfully with default username:", default_username)
    return redirect(reverse('profile'))


@login_required
def create_username(request):
    return render(request, 'create_username.html')


@login_required
def submit_username(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if LeeriApprentices.objects.filter(username=username).exists():
                return render(request, 'create_username.html', {'form': form, 'error': 'Username is already taken'})
            try:
                request.user.username = username
                request.user.save()
                print("Username updated successfully")
                return redirect('profile')  # Redirect to profile page after successful username update
            except Exception as e:
                print("Error updating username:", e)
                return render(request, 'create_username.html',
                              {'form': form, 'error': 'An error occurred while updating the username'})
    else:
        form = MyForm()  # Instantiate an empty form for GET requests

    return render(request, 'create_username.html', {'form': form})  # Render the form
