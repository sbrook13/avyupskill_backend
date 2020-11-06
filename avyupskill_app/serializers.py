from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_jwt.settings import api_settings
from rest_framework import serializers
from . models import (
  Area,  
  Course, 
  BeaconPark,
  User, 
  Comment, 
  Rating, 
  BackcountryDay
)   

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model=User
    fields=('id','username', 'password')
    # extra_kwargs = { 'password': { 'write_only': True} }
  
  def create(self, validated_data):
    validated_data['password'] = make_password(validated_data['password'])
    user = User.objects.create(**validated_data)
    return user


class LoginSerializer(serializers.Serializer):
  username = serializers.CharField(max_length=20)
  password = serializers.CharField(max_length=128, write_only=True)
  token = serializers.CharField(max_length=255, read_only=True)

  def validate(self, data):
    username = data.get("username", None)
    password = data.get("password", None)
    user = authenticate(data, username=username, password=password)
    if user is None:
      raise serializers.ValidationError(
          'Incorrect username and/or password.'
      )
    try:
      payload = api_settings.JWT_PAYLOAD_HANDLER(user)
      jwt_token = api_settings.JWT_ENCODE_HANDLER(payload)
      update_last_login(None, user)
    except User.DoesNotExist:
      raise serializers.ValidationError(
        'User does not exist.'
      )
    return {
      'username': user.username,
      'token': jwt_token
    }


class RatingSerializer(serializers.ModelSerializer):
  class Meta:
    model=Rating
    fields=('id','rating','user', 'area')


class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model=Comment
    fields=('id','feedback','user', 'area')


class BackcountryDaySerializer(serializers.ModelSerializer):
  class Meta:
    model=BackcountryDay
    fields=('id','location','date', 'user', 'area')


class ProfileSerializer(serializers.Serializer):
  comments = CommentSerializer(many=True, required=False)
  ratings = RatingSerializer(many=True, required=False)
  backcountry_days = BackcountryDaySerializer(many=True, required=False)
  def get(self):
    jwt_token = data.get("token", None)
    decoded_token = api_settings.JWT_DECODE_HANDLER(jwt_token)
    fields=(
      'id',
      'username', 
      'first_name', 
      'email', 
      'backcountry_days', 
      'saved_areas', 
      'ratings', 
      'comments'
    )


class AreaSerializer(serializers.ModelSerializer):
  comments = CommentSerializer(many=True, read_only=True)
  ratings = RatingSerializer(many=True, read_only=True)

  class Meta:
    model=Area
    fields=('id','name','description', 'location', 'lon', 'lat', 'comments', 'ratings')


class CourseSerializer(serializers.ModelSerializer):
  class Meta:
    model=Course
    fields=(
      'id',
      'provider',
      'class_type', 
      'location', 
      'start_date', 
      'end_date', 
      'details_url', 
      'aiare_url', 
      'provider_url', 
      'phone', 
      'cost'
    )


class BeaconParkSerializer(serializers.ModelSerializer):
  class Meta:
    model=BeaconPark
    fields=('id','name','lat', 'lon', 'nearest_city' )