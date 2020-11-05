from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser

# Create your models here.
class Area(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=1000)
  location = models.CharField(max_length=100)
  lat = models.CharField(max_length=50, blank=True)
  lon = models.CharField(max_length=50, blank=True)

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

class User(AbstractBaseUser):
    username = models.CharField(
      verbose_name='Username',
      max_length=20,
      unique=True,
    )
    first_name = models.CharField(
      verbose_name='First Name',
      max_length=20,
    )
    email = models.EmailField(
      verbose_name='Email Address',
      max_length=50,
      unique=True,
    )
    areas = models.ManyToManyField(Area, blank=True)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS =('first_name', '')

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
    related_name='user', 
    on_delete=models.CASCADE, 
    verbose_name="The Reviewer",
  )
  area = models.ForeignKey(Area, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.area}: {self.rating}'

class Comment(models.Model):
  feedback = models.CharField(max_length=400)
  user = models.ForeignKey(
    User, 
    related_name='user', 
    on_delete=models.CASCADE, 
    verbose_name="The Reviewer",
  )
  area = models.ForeignKey(Area, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.user}: {self.area}'

class BackcountryDay(models.Model):
  location = models.CharField(max_length=200)
  date = models.DateField()
  user = models.ForeignKey(
    User, 
    related_name='user', 
    on_delete=models.CASCADE, 
  )
  area = models.ForeignKey(Area, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.provider}: {self.class_type} - {self.start_date}'
