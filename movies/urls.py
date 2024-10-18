from . import views
from django.urls import path, include


app_name='movies'
urlpatterns = [
    path('', views.index, name='index'),
  
]