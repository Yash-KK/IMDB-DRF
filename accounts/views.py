from django.shortcuts import render

#REST FRAMEWORK
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

#SERIALIZER
from .serializer import (
    CustomUserSerializer
)

#MODEL
from .models import (
    CustomUser
)
# Create your views here.

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        data = request.data       
        serializer = CustomUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'username': serializer.data['username'],
                'email': serializer.data['email']
            } , status=status.HTTP_200_OK)
               
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        



@api_view(['POST'])
def logout_user(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response({
            'info': "user logged out!"
        }, status=status.HTTP_200_OK)
