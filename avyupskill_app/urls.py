from django.urls import path, include
from . import views
from rest_framework import routers
# from .api import SignupAPI, LoginAPI, CoursesAPI, BeaconParksAPI
from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
router.register('areas', views.AreaView)
router.register('courses', views.CourseView)
router.register('beacon_parks', views.BeaconParkView)
# router.register('users', views.UserView)
# router.register('comments', views.CommentView)
# router.register('ratings', views.RatingView)
# router.register('backcountry_day', views.BackcountryDayView)

urlpatterns = [
  path('', include(router.urls)),
  # path('api/auth/signup', SignupAPI.as_view()),
  # path('api/auth/login', LoginAPI.as_view()),
  # path('api/courses', CoursesAPI.as_view()),
  # path('api/beacon-parks', BeaconParksAPI.as_view()),

]