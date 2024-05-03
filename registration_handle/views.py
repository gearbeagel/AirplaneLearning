from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from opencensus.trace import tracer
from opentelemetry import trace

from profile_page.models import Profile, LearnerType
from registration_handle.forms import ProfileUpdateForm
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    tracer = trace.get_tracer(__name__)

    with tracer.start_as_current_span("homepage") as span:
        span.set_attribute("homepage", request.user.username)
        return render(request, "homepage.html")


def register(request):
    tracer = trace.get_tracer(__name__)

    with tracer.start_as_current_span("register") as span:
        if request.user.is_authenticated:
            user, created = User.objects.get_or_create(user=request.user)
            user.save()
        span.set_attribute("register",request.user.username)
        return render(request, "register.html")


def about(request):
    tracer = trace.get_tracer(__name__)

    with tracer.start_as_current_span("about") as span:
        span.set_attribute("about", request.user.username)
        return render(request, "about.html")


def welcome_email(request):
    user = request.user
    subject = 'Welcome to Airplane Learning!'
    html_message = render_to_string('email_welcome_message.html', {'user': user})
    plain_message = strip_tags(html_message)
    recipient_list = [user.email]

    send_mail(subject, plain_message, None, recipient_list, html_message=html_message, fail_silently=False)
    return redirect('profile_page')


def language_and_learning_path_selection(request):
    tracer = trace.get_tracer(__name__)

    with tracer.start_as_current_span("language_and_learning_path_selection") as span:
        if Profile.objects.filter(user=request.user).exists():
            return redirect('profile_page', username=request.user.username)
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
                    return redirect('profile_page', username=request.user.username)
                except Exception as e:
                    print("Error occurred while creating profile:", e)
            else:
                return HttpResponseBadRequest("Form submission failed. Please check your input.")
        else:
            form = ProfileUpdateForm()
        span.set_attribute('form', form)
        return render(request, 'learning_path_choice.html', {'form': form})
