from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse

from profile_page.models import Profile

@login_required
def profile_page(request):
    student = User.objects.get(email=request.user.email)

    return render(request, 'profile_page.html', {'username': student.username})
