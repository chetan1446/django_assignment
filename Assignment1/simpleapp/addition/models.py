from django.db import models

# Create your models here.
class Assign(models.Model):
    number = models.CharField(null = True, blank=True , max_length=50)
    word = models.CharField(null = True, blank=True , max_length=50)

    def __str__(self)-> str:
        return self.number
