from django.shortcuts import render
from rest_framework.response import Response
from .models import User
from rest_framework.decorators import api_view
from .serializers import UserSerializer

# Create your views here.

# Get all Users


@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

# Get single User


@api_view(['GET'])
def getUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

# Update a User


@api_view(['PUT'])
def updateUser(request, pk):
    data = request.data
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# Create a User
@api_view(['POST'])
def createUser(request):
    data = request.data
    user = User.objects.create(
        first_name=data['first_name'],
        last_name=data['last_name'],
        password=data['password'],
        user_email=data['user_email'],
        user_mobile=data['user_mobile'],
    )
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)
