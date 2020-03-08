from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    #path('/new',views.new),
    #path('/view',views.view),
]
