from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions

from .models import (
  Area,  
  Course, 
  BeaconPark,
)
from .serializers import (
  AreaSerializer,
  CourseSerializer, 
  BeaconParkSerializer,
)
# Create your views here.
class AreaView(viewsets.ModelViewSet):
  queryset = Area.objects.all()
  serializer_class = AreaSerializer

class CourseView(viewsets.ModelViewSet):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer

class BeaconParkView(viewsets.ModelViewSet):
  queryset = BeaconPark.objects.all()
  serializer_class = BeaconParkSerializer