from django.contrib import admin
from .models import (
  Area,  
  Course, 
  BeaconPark,
)

# Register your models here.
admin.site.register(Area)
admin.site.register(Course)
admin.site.register(BeaconPark)
