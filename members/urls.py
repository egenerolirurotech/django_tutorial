"""
URL configuration for members app
"""
from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.member_list, name='member-list'),
    path('members/<int:pk>/', views.member_detail, name='member-detail'),
]
