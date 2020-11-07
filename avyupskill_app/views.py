from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import (
  Area,  
  Course, 
  BeaconPark,
  User, 
  Comment, 
  Rating, 
  BackcountryDay
)

from .serializers import (
  AreaSerializer,
  CourseSerializer, 
  BeaconParkSerializer,
  UserSerializer, 
  ProfileSerializer,
  LoginSerializer,
  CommentSerializer, 
  RatingSerializer, 
  BackcountryDaySerializer,
)
# Create your views here.

class UserView(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

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

    return Response(response, status_code)

class LoginView(CreateAPIView):
  serializer_class = LoginSerializer
  permission_classes = (AllowAny,)

  def post(self, request):
    serializer = self.serializer_class(data = request.data)
    serializer.is_valid(raise_exception = True)
    status_code = status.HTTP_200_OK
    response = {
      'username': serializer.data['username'],
      'token': serializer.data['token'],
      'message': 'User logged in successfully',
      'status': status_code
    }

    return Response(response)


class ProfileView(CreateAPIView):
  serializer_class = ProfileSerializer
  permission_classes = (IsAuthenticated,)

  def list(self, request):
    user = request.user
    serializer = ProfileSerializer(user)
    status_code = status.HTTP_200_OK
    # response = {
    #   'id': serializer.data['id'],
    #   'username': serializer.data['username'],
    #   'first_name': serializer.data['first_name'],
    #   'email': serializer.data['email'],
    #   'backcountry_days': serializer.data['backcountry_days'], 
    #   'saved_areas': serializer.data['saved_areas'],
    #   'ratings': serializer.data['ratings'],
    #   'comments': serializer.data['comments'],
    # }
    return Response(serializer.data, status_code)


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