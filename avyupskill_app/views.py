from django.shortcuts import render
from decouple import config
import requests
import os
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import (
  Area,  
  Course, 
  BeaconPark,
  User, 
  Comment, 
  Rating, 
  BackcountryDay,
  FavoriteArea
)

from .serializers import (
  AreaSerializer,
  CourseSerializer, 
  BeaconParkSerializer,
  UserSerializer, 
  CommentSerializer, 
  RatingSerializer, 
  BackcountryDaySerializer,
  FavoriteAreaSerializer
)
# Create your views here.

class UserView(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [AllowAny,]

class ProfileView(viewsets.ViewSet):
  queryset = User.objects.all()
  def list(self, request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

class AreaView(viewsets.ModelViewSet):
  queryset = Area.objects.all()
  serializer_class = AreaSerializer

class CourseView(viewsets.ModelViewSet):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer

class BeaconParkView(viewsets.ModelViewSet):
  queryset = BeaconPark.objects.all()
  serializer_class = BeaconParkSerializer
  
class CommentView(viewsets.ModelViewSet):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  permission_classes = (IsAuthenticatedOrReadOnly,)

class RatingView(viewsets.ModelViewSet):
  queryset = Rating.objects.all()
  serializer_class = RatingSerializer
  permission_classes = (IsAuthenticatedOrReadOnly,)

class BackcountryDayView(viewsets.ModelViewSet):
  queryset = BackcountryDay.objects.all()
  serializer_class = BackcountryDaySerializer
  permission_classes = (IsAuthenticatedOrReadOnly,)

class FavoriteAreaView(viewsets.ModelViewSet):
  queryset = FavoriteArea.objects.all()
  serializer_class = FavoriteAreaSerializer
  permission_classes = (IsAuthenticatedOrReadOnly,)

class WeatherView(APIView):
  def get(self, request):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat=39.6789&lon=-105.9202&appid={os.environ["WEATHER_KEY"]}&units=imperial'
    r = requests.get(url, headers={'Content-Type': 'application/json'})
    weather = r.json()
    return Response(weather)