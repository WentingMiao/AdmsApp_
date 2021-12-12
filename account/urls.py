from django.contrib import admin
from django.urls import path,include
from account.views import *


urlpatterns = [
    path('login/',account_login,name='login'),
    path('register/',account_register,name='register'),
    path('logout/',account_logout,name='logout'),
    
    path('members/',members_management,name='members'),
    path('members/add/',member_add,name='members_add'),
    path('members/curd/<int:record_id>/',member_curd,name='members_curd'),

    path('users/',users_index,name='users'),
    path('users/add/',users_add,name='users_add'),
    path('users/curd/<int:record_id>/',users_curd,name='users_curd'),
]