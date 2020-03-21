from django.contrib import admin
from .models import TimeSheet


# Register your models here.
class TimesheetAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'time_in', 'time_out', 'num_of_hours', 'status')


admin.site.register(TimeSheet, TimesheetAdmin)
