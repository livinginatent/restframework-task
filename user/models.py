from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=12)
    user_email = models.EmailField(max_length=70, unique=True)
    user_mobile = models.IntegerField()
    

    def __str__(self):
        return f"{self.first_name} {self.last_name} "
