from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser

# Create your models here.
class Course(models.Model):
  CLASSES = (
    ('1', 'AIARE 1 '),
    ('2', 'AIARE 2 '),
    ('3', 'Avalanche Rescue'),
  )
  provider = models.CharField(max_length=100)
  class_type = models.CharField(max_length=30, choices=CLASSES)
  location = models.CharField(max_length=200)
  start_date = models.DateField()
  end_date = models.DateField()
  details_url = models.CharField(max_length=300, blank=True, default="")
  aiare_url = models.CharField(max_length=300, blank=True, default="")
  provider_url = models.CharField(max_length=300, blank=True, default="")
  phone = models.CharField(max_length=30, blank=True, default="")
  contact_email = models.CharField(max_length=100, blank=True, default="")
  cost = models.CharField(max_length=30, blank=True, default="")

  def __str__(self):
    return f'{self.provider}: {self.class_type} - {self.start_date}'
    
class BeaconPark(models.Model):
  name = models.CharField(max_length=200)
  nearest_city = models.CharField(max_length=200)
  lat = models.FloatField(max_length=50)
  lon = models.FloatField(max_length=50)

  def __str__(self):
    return f'{self.id}: {self.name}'


class Area(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=2000)
  location = models.CharField(max_length=100)
  lat = models.FloatField(max_length=50, blank=True)
  lon = models.FloatField(max_length=50, blank=True)

  def __str__(self):
    return f'{self.id}: {self.name}'


class User(AbstractUser):
  first_name = models.CharField(max_length=50, blank=True, null=True)
  areas = models.ManyToManyField(Area, related_name="areas", through='FavoriteArea', blank=True)
  
  def __str__(self):              
    return f'{self.username}'

class Rating(models.Model):
  RATINGS = (
    ('1', 'The Worst'),
    ('2', 'Meh'),
    ('3', 'Average'),
    ('4', 'Yay'),
    ('5', 'The Best'),
  )
  rating = models.CharField(max_length=1, choices=RATINGS)
  user = models.ForeignKey(
    User,
    related_name='rating', 
    on_delete=models.CASCADE, 
    verbose_name="The Reviewer",
  )
  area = models.ForeignKey(Area, related_name='rating', on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.area}: {self.rating}'

class Comment(models.Model):
  feedback = models.TextField(max_length=1000)
  user = models.ForeignKey(
    User, 
    related_name='comment', 
    on_delete=models.CASCADE, 
    verbose_name="The Reviewer",
  )
  area = models.ForeignKey(Area, related_name='comment', on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.user}: {self.area}'


class BackcountryDay(models.Model):
  location = models.CharField(max_length=200)
  journal = models.TextField(max_length=1000)
  date = models.DateField()
  user = models.ForeignKey(
    User, 
    related_name='backcountry_day', 
    on_delete=models.CASCADE, 
  )

  def __str__(self):
    return f'{self.date}: {self.location}'


class FavoriteArea(models.Model):
  user = models.ForeignKey(
    User, 
    related_name='favorite_area', 
    on_delete=models.CASCADE, 
  )
  area = models.ForeignKey(Area, related_name='favorite_area', on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.id}: {self.user} - {self.area}'
