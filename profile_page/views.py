from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from profile_page.forms import ProfileForm
from profile_page.models import Profile
from modules.models import Lesson, Quiz, LessonStatus, QuizStatus


def get_latest_lesson_and_quiz(profile):
    latest_lesson_status = LessonStatus.objects.filter(profile=profile, status='Completed').order_by(
        '-finished_at').first()
    latest_quiz_status = QuizStatus.objects.filter(profile=profile, status='Completed').order_by('-finished_at').first()
    return latest_lesson_status.lesson if latest_lesson_status else None, latest_quiz_status.quiz if latest_quiz_status else None


def calculate_progress(user_profile):
    total_lessons = len(list(Lesson.objects.all()))
    total_quizzes = len(list(Quiz.objects.all()))

    completed_lessons = LessonStatus.objects.filter(profile=user_profile, status="Completed").count()
    completed_quizzes = QuizStatus.objects.filter(profile=user_profile, status="Completed").count()

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
        new_profile = Profile.objects.create(user=request.user, username=request.user.username,
                                             email=request.user.email,
                                             user_id=request.user.id)
        student = new_profile
        calculate_progress(student)

    latest_lesson = LessonStatus.objects.filter(profile=student, status='Completed').order_by('-finished_at').first()
    latest_quiz = QuizStatus.objects.filter(profile=student, status='Completed').order_by('-finished_at').first()

    return render(request, 'profile_page.html', {'student': student, 'user': request.user,
                                                 'latest_lesson': latest_lesson, 'latest_quiz': latest_quiz})


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
