from django.db import models
from django.utils import timezone

# Create your models here.


GENDER_CHOICES = [
    ('Male', 'male'),
    ('Female', 'female'),
]

class Bird(models.Model):
    name= models.CharField(null=True,blank=True,max_length=50)
    species = models.CharField(null=True,blank=True,max_length=50)
    food = models.CharField(null=True,blank=True,max_length=50)
    last_feed_time = models.DateField(default=timezone.now)
    gender = models.CharField(
      choices=GENDER_CHOICES,max_length=10 ,default="male"
    )