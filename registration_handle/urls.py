from django.urls import path

from registration_handle import views

urlpatterns = [
    path('', views.home, name='home'),
    path("setup/", views.language_and_learning_path_selection, name="setup")
]