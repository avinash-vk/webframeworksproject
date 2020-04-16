from . import views
from django.urls import path,include

urlpatterns = [
    path('addpost/',views.addpost,name='addpost'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/update', views.post_update, name='post_update'),
    path('<slug:slug>/delete', views.post_delete, name='post_delete'),
    path('likeSet/<slug:slug>',views.likeSet,name = 'likeSet'),
]
