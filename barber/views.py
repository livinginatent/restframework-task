from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Barber
from .serializers import BarberSerializer

# Create your views here.

# Get all barbers


@api_view(['GET'])
def getBarbers(request):
    barbers = Barber.objects.all()
    serializer = BarberSerializer(barbers, many=True)
    return Response(serializer.data)

# Get single barber


@api_view(['GET'])
def getBarber(request, pk):
    barber = Barber.objects.get(id=pk)
    serializer = BarberSerializer(barber, many=False)
    return Response(serializer.data)

# Update a Barber


@api_view(['PUT'])
def updateBarber(request, pk):
    data = request.data
    barber = Barber.objects.get(id=pk)
    serializer = BarberSerializer(instance=barber, data=data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# Create a Barber

@api_view(['POST'])
def createBarber(request):
    data = request.data
    barber = Barber.objects.create(
        barber_name=data['barber_name'],
        barber_address=data['barber_address'],
        barber_phone=data['barber_phone'],

    )
    serializer = BarberSerializer(barber, many=False)
    return Response(serializer.data)
