from . import views
from django.urls import path

urlpatterns = [
	path('<slug:slug>/detail/', views.workout_detail, name='workout_detail'),
	path('api/addworkout/',views.add_workout,name = "addworkoutha"),
    path('api/workoutupdate/',views.updateworkout,name = "workoutupdate"),
    path('addworkout/',views.addworkout,name='addworkout'),
    path('<slug:slug>/updateworkout/', views.workout_update, name='workout_update'),
    path('<slug:slug>/deleteworkout/', views.workout_delete, name='workout_delete'),
    path('<slug:slug>/', views.workout_comment, name='workout_comment'),
    
    path('likepost/<slug:slug>',views.like_post, name = 'like_work'),
    path('savepost/<slug:slug>',views.save_post, name = 'save_work'),

]
