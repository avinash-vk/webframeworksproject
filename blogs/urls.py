from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name = 'blog-dashboard'),
    #path('/new',views.new),
    #path('/view',views.view),
]
