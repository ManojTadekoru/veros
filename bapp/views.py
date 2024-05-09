from django.shortcuts import render

# Create your views here.
from .serializer import detailsSerializer,transactionSerializer
from .models import details,transaction
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def signup(request):
    serializer=detailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    try:
        user = details.objects.get(email=email, password=password)
    except details.DoesNotExist:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def transaction(request):
    serializer=transactionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

