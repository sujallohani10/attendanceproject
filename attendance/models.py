from  django.conf import settings
from django.db import models

# Create your models here.


class TimeSheet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time_in = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    time_out = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    status = models.IntegerField()
    num_of_hours = models.FloatField(null=True)

    def __str__(self):
        return '%s %s %s' % (self.user, self.time_in, self.time_out)
