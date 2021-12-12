from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('details/<int:pk>/',activity_details,name='activitiy_details'),
    path('index/',activity_index,name='activities'),
    path('create/',activity_create,name='activityCreate'),
    path('edit/<int:pk>/',activity_edit,name='activity_edit'),
    path('delete/<int:pk>/',activity_delete,name='activity_delete'),
    path('register/',activity_register,name='activity_register'),
    path('demo/',activity_demo),
    path('calendar/',activity_calendar,name='activity_calendar'),
    path('application/',activity_application,name='activity_application'),
    path('application/check/',activity_check,name='activity_check'),
    path('application/self/',activity_self,name='activity_self'),
]