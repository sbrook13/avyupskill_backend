from django.contrib import admin
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

# Register your models here.
admin.site.register(Area)
admin.site.register(Course)
admin.site.register(BeaconPark)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(BackcountryDay)
admin.site.register(FavoriteArea)
