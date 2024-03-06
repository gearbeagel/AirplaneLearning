from django.shortcuts import render

# Create your views here.
def all_possible_classes(request):
    return render(request, 'modules_main.html')

