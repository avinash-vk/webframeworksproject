from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.startup, name = 'start-page'),

    path('dashboard/',views.dashboard, name = 'dashboard'),
    path('explore/',views.explore, name = 'explore'),
    path('newsfeed/', views.newsfeed, name = 'newsfeed'),

    path('blogs/',include('blogs.urls'))
]
