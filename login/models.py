from django.db import models
from login.constant import GENDER_CHOICES, ROLE_CHOICES
# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25, null=True)
    phone_number = models.IntegerField(max_length=10, unique=True)
    email_id = models.CharField(max_length=50, null=False)
    gender = models.CharField(choices=GENDER_CHOICES, null=False)
    role = models.CharField(choices=ROLE_CHOICES, null=False)
    username = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    @classmethod
    def soft_delete(cls, customer):
        cls.objects.filter(customer=customer).update(is_deleted=True)
