from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
import pdb

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
  UserProfileSerializer,
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

class UserCreateView(CreateAPIView):
  serializer_class = UserSerializer
  permission_classes = (AllowAny,)

  def post(self, request):
    serializer = self.serializer_class(data = request.data)
    serializer.is_valid(raise_exception = True)
    serializer.save()
    status_code = status.HTTP_201_CREATED

    response = {
      'user': serializer.data,
      'status': status_code,
      'message': 'User created.'
    }

    return Response(response)

class ProfileView(viewsets.ViewSet):
  queryset = User.objects.all()
  def list(self, request):
    serializer = UserProfileSerializer(request.user)
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
  serializer_class = BackcountryDaySerializer
  permission_classes = (IsAuthenticatedOrReadOnly,)