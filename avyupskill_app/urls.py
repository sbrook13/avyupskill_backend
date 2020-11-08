from django.urls import path, include
from rest_framework import routers
from . import views

# from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
router.register('areas', views.AreaView)
router.register('courses', views.CourseView)
router.register('beacon_parks', views.BeaconParkView)
router.register('users', views.UserView)
router.register('comments', views.CommentView)
router.register('ratings', views.RatingView)
router.register('backcountry_days', views.BackcountryDayView)
router.register('favorite_areas', views.FavoriteAreaView)
router.register('profile', views.ProfileView)


urlpatterns = [
  path('signup', views.UserCreateView.as_view()),
  path('', include(router.urls)),
]