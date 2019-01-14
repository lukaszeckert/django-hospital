from django.db import models
from django.core.exceptions import ValidationError

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
        return "Position: {0},Base salary: {1}, Number hours: {2}".format(self.name, self.base_salary, self.number_hours)

class HospitalStaff(models.Model):
    first_name = models.CharField(max_length=40, blank=False, null=False)
    second_name = models.CharField(max_length=40, blank=False, null=False)
    boss_id = models.ForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)
    # TODO add konto bankowe

    def __str__(self):
        boss_id = self.boss_id
        if boss_id is not None:
            boss_id = boss_id.id
        return "First name: {}, Second name: {}, Boss id: {}".format(self.first_name, self.second_name, boss_id)

    def clean(self, *args,**kwargs):
        super().clean(*args, **kwargs)

        self.clean_boss_id()

    def clean_boss_id(self):
        if self.boss_id is not None and self.boss_id.id == self.id:
            raise ValidationError('The boss id can not be equal to employ id.')



class Employment(models.Model):
    position = models.ForeignKey(JobPosition, on_delete=models.PROTECT)
    employ = models.ForeignKey(HospitalStaff, on_delete=models.PROTECT)
    hours = models.FloatField()

    def clean(self):
        super().clean()
        if self.hours <= 0:
            raise ValidationError('Number of hours must be greater than 0.')

    def __str__(self):
        return "Hours: {0} {1}".format(self.hours, self.position)