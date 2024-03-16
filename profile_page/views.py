from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from profile_page.models import LeeriApprentices

@login_required
def profile_page(request):
    email = request.user.email
    try:
        student = LeeriApprentices.objects.get(email=email)
        return render(request, 'profile_page.html', {'username': student.username, 'progress': student.progress})
    except LeeriApprentices.DoesNotExist:
        return redirect('/create_username/')
