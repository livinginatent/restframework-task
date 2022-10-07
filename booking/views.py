from xmlrpc.client import DateTime
from django.shortcuts import render
from rest_framework.response import Response

from user.models import User
from barber.models import Barber
from .models import Booking 
from rest_framework.decorators import api_view
from .serializers import BookingSerializer

# Create your views here.

# Get all bookings


@api_view(['GET'])
def getBookings(request):
    bookings = Booking.objects.all()
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)

# Get single booking


@api_view(['GET'])
def getBooking(request, pk):
    booking = Booking.objects.get(id=pk)
    serializer = BookingSerializer(booking, many=False)
    return Response(serializer.data)


# Get bookings from specific User

@api_view(['GET'])
def getUserBooking(request, pk):
    booking = Booking.objects.filter(customer_id__id = pk)
    serializer = BookingSerializer(booking, many=True)
    return Response(serializer.data)

# Get bookings from specific Barber


@api_view(['GET'])
def getBarberBooking(request, pk):
    booking = Booking.objects.filter(barber_id__id=pk)
    serializer = BookingSerializer(booking, many=True)
    return Response(serializer.data)

# Update booking

@api_view(['PUT'])
def updateBooking(request, pk):
    data = request.data
    booking = Booking.objects.get(id=pk)
    serializer = BookingSerializer(instance=booking, data=data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# Create booking

@api_view(['POST'])
def createBooking(request):
    data = request.data
  
    booking = Booking.objects.create(
       
        customer_id = User.objects.get(id = data['customer_id']),
        barber_id = Barber.objects.get(id = data["barber_id"]),
        timeslot = data['timeslot'],
        )
    serializer = BookingSerializer(booking, many=False)
    return Response(serializer.data)
