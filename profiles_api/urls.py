from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import HelloAPIView, HelloViewSet


router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, base_name='hello-viewset')

urlpatterns = [
    path('hello-view', HelloAPIView.as_view()),
    path('', include(router.urls)),
]