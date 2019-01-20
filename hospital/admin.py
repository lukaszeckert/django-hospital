from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Employment, Employ, JobPosition

admin.site.register(Employment)
admin.site.register(Employ)
admin.site.register(JobPosition)
