from django.urls import path

from . import views
from .views import CreateUser, GetUsers, GetUser, UpdateUser

urlpatterns = [
    path('', GetUsers.as_view(), name='users'),
    path('create/', CreateUser.as_view(), name='create-user'),
    path('user/<str:pk>/', GetUser.as_view(), name='user'),
    path('update/<str:pk>/', UpdateUser.as_view(), name='update-user'), 
]

