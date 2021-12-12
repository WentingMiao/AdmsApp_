from django.urls import path
from .views import *
urlpatterns = [
    path('', index),
    path('profile/<int:id>/',profile_index),
    path('profile/update/<int:id>/',profile_update),
    path('document/profile/',document_profile,name='document_profile'),
    path('document/gallery/',document_gallery,name='document_gallery'),
    path('document/profile/upload/',profile_upload,name='profile_upload'),
    path('document/imgfile/upload/',imgfile_upload,name='imgfile_upload'),
]