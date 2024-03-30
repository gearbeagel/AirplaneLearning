from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
import logging
from modules.models import Language
from profile_page.models import Profile, LearnerType
from registration_handle.forms import ProfileUpdateForm


def home(request):
    return render(request, "homepage.html")


def register(request):
    if request.user.is_authenticated:
        user, created = User.objects.get_or_create(user=request.user)
        user.save()
    return render(request, "register.html")


def about(request):
    return render(request, "about.html")


def language_and_learning_path_selection(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            try:
                Profile.objects.create(
                    user=request.user,
                    chosen_language=form_data['chosen_language'],
                    learner_type=form_data['learner_type']
                )
                return redirect('profile_page')
            except Exception as e:
                print("Error occurred while creating profile:", e)
    else:
        form = ProfileUpdateForm()

    return render(request, 'learning_path_choice.html',
                  {'form': form})
