from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class Area(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=1000)
  location = models.CharField(max_length=100)

  def __str__(self):
    return f'{self.id}: {self.name}'

class Course(models.Model):
  CLASSES = (
    ('1', 'AIARE 1'),
    ('2', 'AIARE 2'),
    ('3', 'Avalanche Rescue'),
  )
  provider = models.CharField(max_length=50)
  class_type = models.CharField(max_length=1, choices=CLASSES)
  location = models.CharField(max_length=200)
  start_date = models.DateField()
  end_date = models.DateField()

  def __str__(self):
    return f'{self.provider}: {self.class_type} - {self.start_date}'
    
class BeaconPark(models.Model):
  name = models.CharField(max_length=200)
  nearest_city = models.CharField(max_length=200)
  lat = models.CharField(max_length=50)
  lon = models.CharField(max_length=50)

  def __str__(self):
    return f'{self.id}: {self.name}'

# class User(AbstractUser):
#     username = models.CharField(
#       verbose_name='Username',
#       max_length=15,
#       unique=True,
#     )
#     first_name = models.CharField(
#       verbose_name='First Name',
#       max_length=15,
#         default=''
#     )
#     email = models.EmailField(
#       verbose_name='Email Address',
#       max_length=60,
#       unique=True,
#     )
#     areas = models.ManyToManyField(Area, blank=True)

#     def __str__(self):              
#       return f'{self.username}'