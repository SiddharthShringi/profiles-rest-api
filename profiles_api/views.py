from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from .models import UserProfile
from .serializers import HelloSerializer, UserProfileSerializer
from .permissions import UpdateOwnProfile


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


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSets"""
    serializer_class = HelloSerializer
    
    def list(self, request):
        return Response({'message': 'hello world!'})

    def create(self, request):
        """Create new object"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message, 'status': status.HTTP_201_CREATED})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        return Response({'message': 'GET', 'status': status.HTTP_200_OK})

    def update(self, request, pk=None):
        return Response({'message': 'PUT', 'status': status.HTTP_200_OK})

    def partial_update(self, request, pk=None):
        return Response({'message': 'PATCH', 'status': status.HTTP_200_OK})

    def destroy(self, request, pk=None):
        return Response({'message': 'DELETE', 'status': status.HTTP_200_OK})


class UserProfileViewSet(viewsets.ModelViewSet):
    "Handle Creating and Updating profile"
    serializer_class = UserProfileSerializer
    permission_classes = (UpdateOwnProfile, )
    authentication_classes = (TokenAuthentication, )
    queryset = UserProfile.objects.all()
