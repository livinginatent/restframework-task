from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.




class Barber(models.Model):
    barber_name = models.CharField(max_length=50, unique=True)
    barber_address = models.CharField(max_length=200, unique=True)
    barber_phone = models.IntegerField()
    def __str__(self):
        return f"{self.barber_name} "


    
