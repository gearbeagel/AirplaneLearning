"""
URL configuration for AirplaneLearning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import modules
from AirplaneLearning import settings
from registration_handle import views as views_reg
from profile_page import views as views_prof
from modules import views as views_mod

urlpatterns = [
    path('', views_reg.home, name='home'),  # Home page
    path('admin/', admin.site.urls),  # Admin interface
    path('register/', views_reg.register, name='register'),  # Registration page
    path('profile/', views_prof.profile_page, name='profile'),
    path("registration_handle/", include("allauth.urls")),
    path('accounts/google/login/callback/', views_reg.callback_view, name='google_callback'),
    path('langs/', include("modules.urls")),
    path('create_username/', views_reg.create_username, name='create_username'),
    path('submit_username/', views_reg.submit_username, name='submit_username'),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
