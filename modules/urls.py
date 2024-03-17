from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ALPP.urls import schema_view
from modules import views

urlpatterns = [
    # Your existing URLs
    path("", views.all_possible_classes, name="all_possible_classes"),
    path("modules_list/<int:language_id>/", views.modules_list, name='modules_list'),
    path("modules_list/<int:language_id>/lesson/<int:lesson_id>/", views.lesson_info, name='lesson_info'),
    path("modules_list/<int:language_id>/quiz/<int:quiz_id>/", views.lesson_quiz, name='lesson_quiz'),
    path("modules_list/<int:language_id>/quiz/<int:quiz_id>/result/", views.quiz_result, name='quiz_result'),

    # Swagger URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]