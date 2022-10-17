from django.urls import path

from . import views

urlpatterns = [
    path('', views.GetBarbers.as_view(), name='barbers'),
    path('create/', views.CreateBarber.as_view(), name='create-barber'),
    path('<str:pk>/', views.GetBarber.as_view(), name='barber'),
    path('update/<str:pk>/', views.UpdateBarber.as_view(), name='update-barber'),
]