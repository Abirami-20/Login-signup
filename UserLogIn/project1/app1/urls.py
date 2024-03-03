
from django.urls import path
from .views import login,register,reg

urlpatterns = [
    path('',login,name='login'),
    path('reg/register',register,name='register'),
    path('reg/',reg),
]