from . import views
from django.urls import path, include


app_name='accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
  
]