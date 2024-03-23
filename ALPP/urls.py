"""
URL configuration for ALPP project.

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
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

import profile_page.views
import registration_handle.views
from ALPP import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Airplane Learning API",
        default_version='v1',
        description="How did you fly in here?",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="kondratskayavictoria@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('modules.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', registration_handle.views.home, name='home'),
    path("accounts/", include("allauth.urls")),
    path('profile/', include("profile_page.urls")),
    path('register/', registration_handle.views.register, name='register'),
    path('langs/', include("modules.urls")),
    path('about/', registration_handle.views.about, name='about')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
