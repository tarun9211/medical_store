from django.db import models
from constant import GENDER_CHOICES, ROLE_CHOICES

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25, null=True)
    phone_number = models.IntegerField(max_length=10, unique=True)
    gender = models.CharField(choices=GENDER_CHOICES, null=False)
    role = models.CharField(choices=ROLE_CHOICES, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    @classmethod
    def soft_delete(cls, customer):
        cls.objects.filter(customer=customer).update(is_deleted=True)


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