from django.db import models
from django.core.exceptions import ValidationError
import datetime


# Create your models here.

class JobPosition(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)
    base_salary = models.IntegerField(blank=False, null=False)
    number_hours = models.IntegerField(blank=False, null=False)

    def clean(self):
        super().clean()

        if self.base_salary < 0:
            raise ValidationError("Base salary can not be negative.")
        if self.number_hours < 0:
            raise ValidationError("Number of hours can not be negative.")

    def __str__(self):
        return "Position: {0},Base salary: {1}, Number hours: {2}".format(self.name, self.base_salary,
                                                                          self.number_hours)


class Employ(models.Model):
    first_name = models.CharField(max_length=40, blank=False, null=False)
    second_name = models.CharField(max_length=40, blank=False, null=False)
    boss_id = models.ForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        boss_id = self.boss_id
        if boss_id is not None:
            boss_id = boss_id.id
        return "First name: {}, Second name: {}, Boss id: {}".format(self.first_name, self.second_name, boss_id)

    def clean(self, *args, **kwargs):
        super().clean(*args, **kwargs)

        self.clean_boss_id()

    def clean_boss_id(self):
        if self.boss_id is not None and self.boss_id.id == self.id:
            raise ValidationError('The boss id can not be equal to employ id.')


class Employment(models.Model):
    position = models.ForeignKey(JobPosition, on_delete=models.PROTECT)
    employ = models.ForeignKey(Employ, on_delete=models.PROTECT)
    hours = models.FloatField()

    def clean(self):
        super().clean()
        if self.hours <= 0:
            raise ValidationError('Number of hours must be greater than 0.')

    def __str__(self):
        return "Hours: {0} {1}".format(self.hours, self.position)


class Patient(models.Model):
    birth_date = models.DateField(blank=False, null=False)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    second_name = models.CharField(max_length=30, blank=False, null=False)
    personal_number = models.CharField(max_length=11, blank=False, null=False)
    nfz_number = models.CharField(max_length=30, blank=True, null=True, default=None)

    def __str__(self):
        return "First name: {}, Second name: {}, Personal number: {}".format(self.first_name, self.second_name, self.personal_number)


class BankAccount(models.Model):
    bank_name = models.CharField(max_length=30, blank=False, null=False)
    number = models.CharField(max_length=20, blank=False, null=False)
    employ = models.ForeignKey(Employ, on_delete=models.PROTECT, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, null=True)


class Appointment(models.Model):
    date = models.DateField()
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, null=False)
    employ = models.ForeignKey(Employ, on_delete=models.PROTECT, null=False)
    description = models.CharField(max_length=100, blank=True, null=True)


class FamilyDoctor(models.Model):
    type = models.CharField(max_length=30, blank=False, null=False)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, null=False)
    employ = models.ForeignKey(Employ, on_delete=models.PROTECT, null=False)


class Department(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    chief = models.ForeignKey(Employ, on_delete=models.PROTECT)


class HospitalRoom(models.Model):
    places = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.PROTECT)

    def __str__(self):
        return "ID: {}, Places: {}, Department: {}".format(self.id, self.places, self.department.name)


class Residence(models.Model):
    beginning_date = models.DateField(default=datetime.date.today, null=False)
    end_date = models.DateField(null=True)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)
    room = models.ForeignKey(HospitalRoom, on_delete=models.PROTECT)
