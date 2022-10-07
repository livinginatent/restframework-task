from django.urls import path
from .views import createBooking, getBarberBooking, getBooking, getBookings, getUserBooking, updateBooking

urlpatterns = [
    path('', view=getBookings, name='bookings'),
    path('create/', view=createBooking, name='create-booking'),
    path('<str:pk>/', view=getBooking, name='booking'),
    path('update/<str:pk>/', view=updateBooking, name='update-booking'),
    path('user-booking/<str:pk>/', view=getUserBooking, name='user-booking'),
    path('barber-booking/<str:pk>/', view=getBarberBooking, name='barber-booking'),
]