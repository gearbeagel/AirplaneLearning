from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from profile_page.models import Profile, LearnerType
from registration_handle.forms import ProfileUpdateForm
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    return render(request, "homepage.html")


def register(request):
    if request.user.is_authenticated:
        user, created = User.objects.get_or_create(user=request.user)
        user.save()
    return render(request, "register.html")


def about(request):
    return render(request, "about.html")


def welcome_email(request):
    user = request.user
    subject = 'Welcome to Airplane Learning!'
    message = f'{user.username}, thanks for becoming a part of our community!'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    return redirect('profile_page')


def language_and_learning_path_selection(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            try:
                Profile.objects.create(
                    user=request.user,
                    email=request.user.email,
                    username=request.user.username,
                    user_id=request.user.id,
                    chosen_language=form_data['chosen_language'],
                    learner_type=form_data['learner_type']
                )
                welcome_email(request)
                return redirect('profile_page')
            except Exception as e:
                print("Error occurred while creating profile:", e)
        else:
            return HttpResponseBadRequest("Form submission failed. Please check your input.")
    else:
        form = ProfileUpdateForm()

    return render(request, 'learning_path_choice.html', {'form': form})
