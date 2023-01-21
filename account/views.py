from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializer import (
    UserSerializer
)

# Create your views here.

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        # Deleted the Token i.e Logout 
        request.user.auth_token.delete()
        return Response({
            'detail':'Successfully Logged Out'
        }, status=status.HTTP_200_OK)