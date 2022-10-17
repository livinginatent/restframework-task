
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import CreateView


from barber.models import Barber
from user.models import User
from .models import Booking


# Create your views here.


# Get all bookings


class GetBookings(ListView):
    template_name = "booking_list.html"
    model = Booking


# Get single booking

class GetBooking(DetailView):
    model = Booking
    template_name = "single_booking.html"


# Get bookings from specific User

class GetUserBooking(DetailView):
    model = User
    template_name = "user_booking.html"


# Get bookings from specific Barber

class GetBarberBooking(DetailView):
    model = Barber
    template_name = "barber_booking.html"

# Update booking


class UpdateBooking(UpdateView):
    model = Booking
    fields = ('customer', 'barber',  'timeslot')
    
    template_name = "user_update.html"


# Create booking

class CreateBooking(CreateView):
    model = Booking

    fields = '__all__'
    template_name = "create_booking.html"
