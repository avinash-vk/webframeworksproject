from . import views
from django.urls import path

urlpatterns = [
    path('addpicture/',views.addpicture,name='addpicture'),
    path('<slug:slug>/updatepicture/', views.picture_update, name='picture_update'),
    path('<slug:slug>/deletepicture/', views.picture_delete, name='picture_delete'),
    path('<slug:slug>/', views.picture_comment, name='picture_comment'),

]