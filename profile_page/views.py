from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from modules.models import Lesson
from profile_page.models import Profile
from django.db.models import Q


def calculate_progress(user_profile):
    total_lessons = Lesson.objects.count()

    completed_lessons = Lesson.objects.filter(Q(status='completed') | Q(status='Completed')).count()

    if total_lessons > 0:
        progress_percentage = (completed_lessons / total_lessons) * 100
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
        calculate_progress(student)

    return render(request, 'profile_page.html', {'student': student, 'user': request.user})
