
from django.db import models
from django.urls import reverse

# Create your models here.

class Barber(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=200, unique=False)
    phone = models.IntegerField()
    def __str__(self):
        return f"{self.name} "
    
    def get_absolute_url(self):  # new
        return reverse('barber', args=[str(self.id)])


    
