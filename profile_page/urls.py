from django.urls import path

from profile_page import views

urlpatterns = [
    path("", views.profile_page, name="profile_page"),
    path('settings/', views.profile_settings, name="profile_settings")
]