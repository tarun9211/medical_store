from django.db import models
from constant import GENDER_CHOICES, ROLE_CHOICES
from login.models import Customer
# Create your models here.

class Medicine(models.Model):
    name = models.CharField(max_length=50)

class PrescriptionHistory(models.Model):
    doctor = models.ForeignKey(Customer, on_delete=models.CASCADE)
    patient = models.ForeignKey(Customer, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)

class Appointment(models.Model):
    doctor = models.ForeignKey(Customer, on_delete=models.CASCADE)
    patient = models.ForeignKey(Customer, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    date = models.CharField(max_length=10)
    time = models.CharField(max_length=10)