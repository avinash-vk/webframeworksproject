from . import views
from django.urls import path,include

urlpatterns = [

    # path('addpost/',views.addpost,name='addpost'),
    path('addblog/', views.addblog, name = 'addpost'),
    path('updateblog/<slug:slug>/',views.updateblog,name = 'post_update'),
    path('api/addpost/', views.add_post, name = 'addposttha'),
    path('api/updatepost/',views.updatepost,name = 'updateposttha'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    #path('<slug:slug>/update', views.post_update, name='post_update'),
    #path('addpost/',views.addpost,name='addpost'),
    path('<slug:slug>/', views.blog_comment, name='blog_comment'),
    #path('<slug:slug>/update', views.post_update, name='post_update'),
    path('<slug:slug>/delete', views.post_delete, name='post_delete'),
    path('likeblog/<slug:slug>',views.like_post,name = "like_blog"),
    path('saveblog/<slug:slug>',views.save_post,name = "save_blog")
]
