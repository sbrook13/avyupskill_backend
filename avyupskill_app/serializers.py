from django.contrib.auth.hashers import make_password
from rest_framework import serializers
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

class UserObjectSerializer(serializers.ModelSerializer):
  class Meta:
    model=User
    fields=('id','username','password', 'first_name', 'fav_areas')


class AreaObjectSerializer(serializers.ModelSerializer):
  class Meta:
    model=Area
    fields=('id','name','description', 'location', 'lon', 'lat')


class RatingObjectSerializer(serializers.ModelSerializer):
  user = UserObjectSerializer(many=False)

  class Meta:
    model=Rating
    fields=('id','user')


class CommentObjectSerializer(serializers.ModelSerializer):
  user = UserObjectSerializer(many=False)

  class Meta:
    model=Comment
    fields=('id','feedback','user')

class FavoriteAreaObjectSerializer(serializers.ModelSerializer):
  # user = UserObjectSerializer(many=False)
  area = AreaObjectSerializer(many=False)
  
  class Meta:
    model=FavoriteArea
    fields=('id', 'area')


class BackcountryDayObjectSerializer(serializers.ModelSerializer):
  user = UserObjectSerializer(many=False)

  class Meta:
    model=BackcountryDay
    fields=('id','location','journal', 'date', 'user')


class AreaSerializer(serializers.ModelSerializer):
  comments = CommentObjectSerializer(many=True, read_only=True)
  ratings = RatingObjectSerializer(many=True, read_only=True)

  class Meta:
    model=Area
    fields=('id','name','description', 'location', 'lon', 'lat', 'comments', 'ratings')


class UserSerializer(serializers.ModelSerializer):
  fav_areas = FavoriteAreaObjectSerializer(many=True, required=False)
  comments = CommentObjectSerializer(many=True, required=False)
  ratings = RatingObjectSerializer(many=True, required=False)
  backcountry_days = BackcountryDayObjectSerializer(many=True, required=False)

  class Meta:
    model=User
    fields=('id', 'username', 'password', 'first_name', 'fav_areas', 'comments', 'ratings', 'backcountry_days')
    extra_kwargs = { 'password': { 'write_only': True} }
  
  def create(self, validated_data):
    user = User.objects.create(
      username = validated_data['username'],
      password = make_password(validated_data['password']),
    )
    
    return user  

class RatingSerializer(serializers.ModelSerializer):
  class Meta:
    model=Rating
    fields=('id','rating','user', 'area')


class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model=Comment
    fields=('id','feedback','user', 'area')

class FavoriteAreaSerializer(serializers.ModelSerializer):
  class Meta:
    model=FavoriteArea
    fields=('id','user', 'area')


class BackcountryDaySerializer(serializers.ModelSerializer):
  class Meta:
    model=BackcountryDay
    fields=('id','location','date', 'user', 'journal')


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
    fields=('id','name','lat', 'lon', 'location', 'description' )