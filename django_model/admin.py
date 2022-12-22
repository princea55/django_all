from django.contrib import admin

from django_model.models import Employee, Timesheet, Fruit

# Register your models here.
admin.site.register(Employee)
admin.site.register(Timesheet)
admin.site.register(Fruit)