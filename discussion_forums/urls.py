from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_forum_page, name='main_forum_page'),
    path('create/', views.add_topic, name='add_topic'),
    path('<int:topic_id>/', views.topic_page, name='topic_page'),
    path('<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]