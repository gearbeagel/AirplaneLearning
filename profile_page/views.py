from django.http import HttpResponse
from django.shortcuts import render

"""from profile_page.models import User


# Create your views here.
def profile_page(request, given_name):
    profile_get = User.objects.get(first_name=given_name)
    profile_info ={
        'first_name': given_name,
        'last_name': profile_get.last_name
    }

    return render(request, "profile_page.html", {"profile_info": profile_info})"""

def profile_page(request):
    return HttpResponse("This is your profile. Hi!")