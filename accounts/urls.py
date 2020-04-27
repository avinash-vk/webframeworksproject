
from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [

    path('login/',views.loginUser, name = 'login'),
    path('register/',views.register, name = 'register'),
    path('trainer_register/', views.trainer_register, name = 'trainer-register'),
    path('trainee_register/',views.trainee_register,name = 'trainee-register'),
    path('logout/',views.logoutUser,name = 'logout'),
    path('formslol/', views.formstart , name = 'forms'),
    path('api/updatebio/', views.updatebio, name = 'updatebio'),
    path('api/addbio/', views.addbio, name ='addbio'),
    path('',include('feed.urls')),
]
