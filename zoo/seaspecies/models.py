from django.db import models
from django.utils import timezone

# Create your models here.


class Fish(models.Model):
    colour= models.CharField(null=True,blank=True,max_length=50)
    species = models.CharField(null=True,blank=True,max_length=50)
    food = models.CharField(null=True,blank=True,max_length=50)
    last_feed_time = models.DateField(default=timezone.now)
