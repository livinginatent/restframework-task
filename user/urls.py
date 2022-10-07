from django.urls import path
from .views import createUser, getUser, getUsers, updateUser

urlpatterns = [
    path('', view=getUsers, name='users'),
    path('create/', view=createUser, name='create-user'),
    path('<str:pk>/', view=getUser, name='user'), 
    path('update/<str:pk>/', view=updateUser, name='update-user'), 
]

