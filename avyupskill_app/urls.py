from django.urls import path, include
from . import views
from rest_framework import routers
from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
router.register('areas', views.AreaView)
router.register('courses', views.CourseView)
router.register('beacon_park', views.BeaconParkView)

urlpatterns = [
  path('', include(router.urls))
]