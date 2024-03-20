from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from profile_page.forms import ProfileForm
from profile_page.models import Profile
from modules.models import Lesson, Quiz


def calculate_progress(user_profile):
    total_lessons = Lesson.objects.count()
    total_quizzes = Quiz.objects.count()

    completed_lessons = Lesson.objects.filter(status="Completed").count()
    completed_quizzes = Quiz.objects.filter(status="Completed").count()

    total_items = total_lessons + total_quizzes
    completed_items = completed_lessons + completed_quizzes

    if total_items > 0:
        progress_percentage = (completed_items / total_items) * 100
    else:
        progress_percentage = 0

    user_profile.progress = progress_percentage
    user_profile.save()


@login_required
def profile_page(request):
    try:
        student = Profile.objects.get(user=request.user)
        calculate_progress(student)
    except Profile.DoesNotExist:
        new_profile, created = Profile.objects.get_or_create(user=request.user)
        student = new_profile
        student.save()
        calculate_progress(student)

    return render(request, 'profile_page.html', {'student': student, 'user': request.user})


@login_required()
def profile_settings(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile_settings.html', {'form': form})


@login_required()
def logout_page(request):
    logout(request)
    return redirect('/')