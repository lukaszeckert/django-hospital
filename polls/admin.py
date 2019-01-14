from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Employment, HospitalStaff, JobPosition

admin.site.register(Employment)
admin.site.register(HospitalStaff)
admin.site.register(JobPosition)
