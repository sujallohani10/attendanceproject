from django.db import models


# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    contact_info = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    profile_photo = models.CharField(max_length=100)
    joined_date = models.DateField(auto_now=False, auto_now_add=False)
    status = models.IntegerField(default=1)
    created_on = models.DateTimeField(auto_now_add=True)
