"""
URL configuration for members app
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MemberViewSet  # Import your custom ViewSet

# Initialize DRF router instance
router: DefaultRouter = DefaultRouter()

# register the MemberViewSet undert the route 'members'
# this will auto-generate routes:
# - /members/
# - /members/{pk}/
# - /members/{pk}/activate/
router.register(r'members', MemberViewSet, basename='member')

urlpatterns = [
    path('', include(router.urls)),
]
