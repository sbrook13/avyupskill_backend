from django.urls import path, include
from .views import (
  UserCreateView, 
  UserView, 
  LoginView,
  AreaView,
  CommentView,
  RatingView,
  CourseView,
  BackcountryDayView,
  BeaconParkView
)
from rest_framework import routers
# from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
router.register('areas', AreaView)
router.register('courses', CourseView)
router.register('beacon_parks', BeaconParkView)
router.register('users', UserView)
router.register('comments', CommentView)
router.register('ratings', RatingView)
router.register('backcountry_day', BackcountryDayView)

urlpatterns = [
  path('signup', UserCreateView.as_view()),
  path('login', LoginView.as_view()),
  path('', include(router.urls)),
]