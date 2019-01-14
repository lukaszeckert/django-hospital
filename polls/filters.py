from django.contrib.auth.models import User
import django_filters
from .models import *


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', ]


class EmployeesFilter(django_filters.FilterSet):
    class Meta:
        model = HospitalStaff
        fields = '__all__'


class JobPositionFilter(django_filters.FilterSet):
    class Meta:
        model = JobPosition
        fields = '__all__'
