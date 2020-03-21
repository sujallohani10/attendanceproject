from django.contrib import admin
from employee.models import Employee


# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'address', 'birth_date', 'contact_info', 'profile_photo', 'status', 'joined_date')


admin.site.register(Employee, EmployeeAdmin)
