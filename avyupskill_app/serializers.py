from rest_framework import serializers
from . models import (
  Area,  
  Course, 
  BeaconPark,
)

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