from django.urls import path
from . import views


urlpatterns = [
    path('', views.GetBookings.as_view(), name='bookings'),
    path('create/', views.CreateBooking.as_view(), name='create-booking'),
    path('<str:pk>/', views.GetBooking.as_view(), name='booking'),
    path('update/<str:pk>/', views.UpdateBooking.as_view(), name='update-booking'),
    path('user-booking/<str:pk>/', views.GetUserBooking.as_view(), name='user-booking'),
    path('barber-booking/<str:pk>/', views.GetBarberBooking.as_view(), name='barber-booking'),
]