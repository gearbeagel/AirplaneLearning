from django.urls import path

from registration_handle import views

urlpatterns = [
    path("setup/", views.learning_path_selection, name="setup")
]