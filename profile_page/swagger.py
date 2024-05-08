import json

from django.http import HttpResponse, JsonResponse
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, status
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


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_info(request):
    try:
        user = request.user
        profile = Profile.objects.get(user=user)

        learner_type_name = str(profile.learner_type)
        chosen_language_name = str(profile.chosen_language)

        user_info = {
            'username': user.username,
            'progress': profile.progress,
            'profile_pic_url': profile.profile_pic_url.url if profile.profile_pic_url else None,
            'learner_type': learner_type_name,
            'chosen_language': chosen_language_name,
        }

        prettified_json = json.dumps(user_info, indent=4)

        return JsonResponse(json.loads(prettified_json), safe=False)
    except Profile.DoesNotExist:
        return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND,
                        content_type='application/json')
