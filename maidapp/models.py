from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MaidUserProfile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    mobile_number = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    monthly_Charge = models.FloatField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name
