from rest_framework import serializers
from . models import (
  Area,  
  Course, 
  BeaconPark,
  # User, 
  # Comment, 
  # Rating, 
  # BackcountryDay
)

# class SignupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'password', 'name', 'phone')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)

#         return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Email and/or password is incorrect')

# class RatingSerializer(serializers.ModelSerializer):
#   class Meta:
#     model=Rating
#     fields=('id','rating','user', 'area')

# class CommentSerializer(serializers.ModelSerializer):
#   class Meta:
#     model=Comment
#     fields=('id','feedback','user', 'area')

# class BackcountryDaySerializer(serializers.ModelSerializer):
#   class Meta:
#     model=BackcountryDay
#     fields=('id','location','date', 'user', 'area')
    
# class UserSerializer(serializers.ModelSerializer):
#   # comments = CommentSerializer(many=True)
#   # ratings = RatingSerializer(many=True)
#   # backcountry_days = BackcountryDaySerializer(many=True)
  
#   class Meta:
#     model=User
#     fields=('id','password', 'email', 'first_name', 'areas')

class AreaSerializer(serializers.ModelSerializer):
  # comments = CommentSerializer(many=True, read_only=True)
  # ratings = RatingSerializer(many=True, read_only=True)

  class Meta:
    model=Area
    fields=('id','name','description', 'location')

class CourseSerializer(serializers.ModelSerializer):
  class Meta:
    model=Course
    fields=('id','provider','class_type', 'location', 'start_date', 'end_date')

class BeaconParkSerializer(serializers.ModelSerializer):
  class Meta:
    model=BeaconPark
    fields=('id','name','lat', 'lon', 'nearest_city' )