from django.urls import path
from .views import *
urlpatterns = [
    path('', index),
    path('profile/<int:id>/',profile_index),
    path('profile/update/<int:id>/',profile_update),
    path('document/profile/',document_profile,name='document_profile'),
    path('document/profile/upload/',profile_upload,name='profile_upload'),
]