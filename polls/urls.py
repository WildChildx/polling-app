from django.urls import path
from django.urls.resolvers import URLPattern

from  . import views

urlpatterns = [
    path('',views.index),
    path('<str:question_id>/',views.details),
    path('vote/<str:question_id>/',views.vote),
    path('result/<str:question_id>/',views.result)
]