from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Test API View"""
    
    def get(self, request, format=None):
        """Return an Hello message"""
        return Response({'message': 'hello world!'})