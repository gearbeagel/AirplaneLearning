from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from modules import views

urlpatterns = [
    path("", views.all_possible_classes, name="all_possible_classes"),
    path("modules_list/<int:language_id>/", views.modules_list, name='modules_list'),
    path("modules_list/<int:language_id>/<int:lesson_id>", views.lessons, name='lesson_info')
]
