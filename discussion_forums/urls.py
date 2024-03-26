from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_forum_page, name='main_forum_page'),
    path('create/', views.add_topic, name='add_topic'),
    path('<int:topic_id>/', views.forum_page_with_topics, name='topic_page')
]