<<<<<<< HEAD
from . import views
from django.urls import path

urlpatterns = [
    path('addpost/',views.addpost,name='addpost'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/update', views.post_update, name='post_update'),
    path('<slug:slug>/delete', views.post_delete, name='post_delete')
=======
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    #path('/new',views.new),
    #path('/view',views.view),
>>>>>>> ef99cff9e7ad8f0fb4d1fe66578540b18f16eb55
]
