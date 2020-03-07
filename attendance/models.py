from  django.conf import settings
from django.db import models

# Create your models here.


class TimeSheet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    signin_datetime = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    signout_datetime = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
