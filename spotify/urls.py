from . import views
from django.urls import path

urlpatterns = [
    path('addplaylist/',views.add_playlist,name='addplaylist'),

]
