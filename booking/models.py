from email.policy import default
from django.urls import reverse
from tkinter import CASCADE
from django.db import models
from barber.models import Barber
from user.models import User

# Create your models here.


class Booking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE )
    timeslot = models.DateTimeField('appointment')

    def __str__(self):
        return f"{self.customer} {self.barber} {self.timeslot}"

    def get_absolute_url(self):  # new
        return reverse('booking', args=[str(self.id)])
