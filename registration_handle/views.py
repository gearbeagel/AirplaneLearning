from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse
from google.oauth2 import id_token
from google.auth.transport import requests
from models import User


# Create your views here.
def home(request):
    return render(request, "homepage.html")


def register(request):
    return render(request, "register.html")

def callback_view(request):
    if 'id_token' in request.POST:
        token = request.POST['id_token']
        try:
            idinfo = id_token.verify_oauth2_token(token, requests.Request())

            email = idinfo['email']
            first_name = idinfo['given_name']
            last_name = idinfo['family_name']

            user, created = User.objects.get_or_create(email=email, defaults={
                'first_name': first_name,
                'last_name': last_name
            })
            if created:
                user.registration_method = 'google'
                user.save()

            login(request, user)

            return redirect(reverse('all_possible_classes'))
        except ValueError:
            pass

    return redirect(reverse('home'))

