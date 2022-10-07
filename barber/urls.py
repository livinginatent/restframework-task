from django.urls import path

from . views import getBarbers, getBarber, updateBarber, createBarber

urlpatterns = [
    path('', view=getBarbers, name='barbers'),
    path('create/', view=createBarber, name='create-barber'),
    path('<str:pk>/', view=getBarber, name='barber'),
    path('update/<str:pk>/', view=updateBarber, name='update-barber'),
]