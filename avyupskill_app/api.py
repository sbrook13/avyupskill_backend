from rest_framework import generics, permissions, filters
from rest_framework.response import Response
# from knox.models import AuthToken
from .models import (
  Area,  
  Course, 
  BeaconPark,
  # User, 
  # Comment, 
  # Rating, 
  # BackcountryDay
)

from .serializers import (
  AreaSerializer,
  CourseSerializer, 
  BeaconParkSerializer,
  # UserSerializer, 
  # CommentSerializer, 
  # RatingSerializer, 
  # BackcountryDaySerializer,
)

# class SignupAPI(generics.GenericAPIView):
#     serializer_class = SignupSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
        
#         _, token = AuthToken.objects.create(user)
#         return Response({
#             "user": UserSerializer(user, context=self.get_serializer_context()).data,
#             "token": token
#         })

# class LoginAPI(generics.GenericAPIView):
#     serializer_class = LoginSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data
        
#         _, token = AuthToken.objects.create(user)
#         return Response({
#             "user": UserSerializer(user, context=self.get_serializer_context()).data,
#             "token": token
#         })

# class FriendSearchAPI(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = FriendsSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['name', '=phone', 'username']

# class PartyRestaurantsAPI(generics.ListAPIView):
#     queryset = LikedRestaurant.objects.all()
#     serializer_class = LikedRestaurantSerializer

#     def get_queryset(self):
#         queryset = LikedRestaurant.objects.all()
#         party = self.request.query_params.get('party_id', None)
#         if party is not None:
#             queryset = queryset.filter(party_id=party)
#         return queryset

# class MatchedRestaurantsAPI(generics.ListAPIView):
#     queryset = MatchedRestaurant.objects.all()
#     serializer_class = MatchedRestaurantSerializer

#     def get_queryset(self):
#         queryset = MatchedRestaurant.objects.all()
#         party = self.request.query_params.get('party_id', None)
#         if party is not None:
#             queryset = queryset.filter(party_id=party)
#         return queryset
