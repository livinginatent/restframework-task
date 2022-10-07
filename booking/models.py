
from tkinter import CASCADE
from django.db import models
from barber.models import Barber
from user.models import User

# Create your models here.

class Booking(models.Model):
    customer_id = models.ForeignKey(User, on_delete = models.CASCADE,)
    barber_id = models.ForeignKey(Barber, on_delete = models.CASCADE)
    timeslot = models.DateTimeField('appointment')

    def __str__(self):
        return f"{self.customer_id} {self.barber_id} {self.timeslot}"
