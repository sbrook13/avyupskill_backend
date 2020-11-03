from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions

from .models import (
  Area,  
  Course, 
  BeaconPark,
  # User, 
  # Comment, 
  # Rating, 
  # BackcountryDay
)

from .serializers import (
  AreaSerializer,
  CourseSerializer, 
  BeaconParkSerializer,
  # UserSerializer, 
  # CommentSerializer, 
  # RatingSerializer, 
  # BackcountryDaySerializer,
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

# class UserView(viewsets.ModelViewSet):
#   queryset = User.objects.all()
#   serializer_class = UserSerializer
  
# class CommentView(viewsets.ModelViewSet):
#   queryset = Comment.objects.all()
#   serializer_class = CommentSerializer
#   permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# class RatingView(viewsets.ModelViewSet):
#   queryset = Rating.objects.all()
#   serializer_class = RatingSerializer
#   permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# class BackcountryDayView(viewsets.ModelViewSet):
#   queryset = BackcountryDay.objects.all()
#   serializer_class = BackcountryDaySerializer
#   permission_classes = (permissions.IsAuthenticated)