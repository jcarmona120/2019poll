from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^questionlist', views.question_list, name='question_list'),
    re_path(r'^vote', views.vote, name='vote')
]
