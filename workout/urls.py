from . import views
from django.urls import path

urlpatterns = [
    path('addworkout/',views.addworkout,name='addworkout'),
    path('<slug:slug>/updateworkout/', views.workout_update, name='workout_update'),
    path('<slug:slug>/deleteworkout/', views.workout_delete, name='workout_delete'),
    path('<slug:slug>/', views.workout_comment, name='workout_comment'),

]