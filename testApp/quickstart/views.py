from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from testApp.quickstart.serializers import GroupSerializer, UserSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    # API Endpoint to view and edit users
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    # API endpoint for groups
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
