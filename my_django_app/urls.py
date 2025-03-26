"""
URL configuration for my_django_app app
"""

from django.urls import path
from . import views

urlpatterns = [
    path('myapp/', views.myapp, name='myapp'),
]
