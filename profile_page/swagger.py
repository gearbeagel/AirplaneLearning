import json

from django.http import HttpResponse, JsonResponse
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, status, serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Profile

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
    permission_classes=([permissions.IsAuthenticated])
)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'username', 'email', 'chosen_language_id', 'profile_pic_url']