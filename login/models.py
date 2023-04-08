from django.db import models
from home.models import Customer
# Create your models here.

class LoginCredentials(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    username = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=50)