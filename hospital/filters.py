from django.contrib.auth.models import User
import django_filters
from .models import *


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', ]


class EmployFilter(django_filters.FilterSet):
    class Meta:
        model = Employ
        fields = '__all__'


class JobPositionFilter(django_filters.FilterSet):
    class Meta:
        model = JobPosition
        fields = '__all__'


class EmploymentFilter(django_filters.FilterSet):
    class Meta:
        model = Employment
        fields = '__all__'


class PatientFilter(django_filters.FilterSet):
    class Meta:
        model = Patient
        fields = '__all__'


class BankAccountFilter(django_filters.FilterSet):
    class Meta:
        model = BankAccount
        fields = '__all__'


class AppointmentFilter(django_filters.FilterSet):
    class Meta:
        model = Appointment
        fields = '__all__'


class FamilyDoctorFilter(django_filters.FilterSet):
    class Meta:
        model = FamilyDoctor
        fields = '__all__'


class DepartmentFilter(django_filters.FilterSet):
    class Meta:
        model = Department
        fields = '__all__'


class HospitalRoomFilter(django_filters.FilterSet):
    class Meta:
        model = HospitalRoom
        fields = '__all__'


class ResidenceFilter(django_filters.FilterSet):
    class Meta:
        model = Residence
        fields = '__all__'
