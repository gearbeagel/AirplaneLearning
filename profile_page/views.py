from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from profile_page.models import LeeriApprentices


@login_required
def profile_page(request):
    username = request.user.username
    try:
        student = LeeriApprentices.objects.get(username=username)
        progress = student.progress
    except LeeriApprentices.DoesNotExist:
        redirect('submit_username')

    return render(request, 'profile_page.html', {'username': username, 'progress': progress})
