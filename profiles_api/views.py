from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import HelloSerializer


class HelloAPIView(APIView):
    """Test API View"""
    serializer_class = HelloSerializer
    
    def get(self, request, format=None):
        """Return an Hello message"""
        return Response({'message': 'hello world!'})

    def post(self, request):
        """Create a hello message with the requested name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message, 'status': status.HTTP_200_OK})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({'method': 'PUT', 'status': status.HTTP_200_OK})

    def patch(self, request, pk=None):
        return Response({'method': 'PATCH', 'status': status.HTTP_200_OK})

    def delete(self, request, pk=None):
        return Response({'method': 'DELETE', 'status': status.HTTP_200_OK})