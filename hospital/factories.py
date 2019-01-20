from .models import *
import factory


class EmployFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Employ

    first_name = factory.Faker('first_name')
    second_name = factory.Faker('last_name')


class EmployWithBossFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Employ

    first_name = factory.Faker('first_name')
    second_name = factory.Faker('last_name')
    boss = factory.Iterator(Employ.objects.all())


class JobPositionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = JobPosition

    name = factory.Faker('word')
    base_salary = factory.Faker('random_int')
    number_hours = 40


class EmploymentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Employment

    position = factory.Iterator(JobPosition.objects.all())
    employ = factory.Iterator(Employ.objects.all())
    hours = factory.Faker('random_digit')


class PatientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Patient

    birth_date = factory.Faker('date')
    first_name = factory.Faker('first_name')
    second_name = factory.Faker('last_name')
    personal_number = '99999999999'
    nfz_number = '9999999999999999999'


class BankAccountFactoryPatient(factory.DjangoModelFactory):
    class Meta:
        model = BankAccount

    bank_name = factory.Faker('word')
    number = factory.Faker('credit_card_number')
    patient = factory.Iterator(Patient.objects.all())


class BankAccountFactoryEmploy(factory.DjangoModelFactory):
    class Meta:
        model = BankAccount

    bank_name = factory.Faker('word')
    number = factory.Faker('credit_card_number')
    employ = factory.Iterator(Employ.objects.all())


class AppointmentFactory(factory.DjangoModelFactory):
    class Meta:
        model = Appointment

    date = factory.Faker('date')
    patient = factory.Iterator(Patient.objects.all())
    employ = factory.Iterator(Employ.objects.all())
    description = factory.Faker('sentence')


class FamilyDoctorFactory(factory.DjangoModelFactory):
    class Meta:
        model = FamilyDoctor

    type = factory.Faker('word')
    patient = factory.Iterator(Patient.objects.all())
    employ = factory.Iterator(Employ.objects.all())


class DepartmentFactory(factory.DjangoModelFactory):
    class Meta:
        model = Department

    name = factory.Faker('word')
    chief = factory.Iterator(Employ.objects.all())


class HospitalRoomFactory(factory.DjangoModelFactory):
    class Meta:
        model = HospitalRoom

    places = factory.Faker('random_number')
    department = factory.Iterator(Department.objects.all())


class ResidenceFactory(factory.DjangoModelFactory):
    class Meta:
        model = Residence

    beginning_date = factory.Faker('date')
    patient = factory.Iterator(Patient.objects.all())
    room = factory.Iterator(HospitalRoom.objects.all())
