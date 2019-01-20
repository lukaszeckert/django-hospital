from django.core.management.base import BaseCommand, CommandError
from ...factories import *
from faker import Faker


class Command(BaseCommand):
    help = 'Populates database with dummy values'

    def add_arguments(self, parser):
        parser.add_argument('n', nargs='+', type=int)

    def handle(self, *args, **options):

        for _ in range(options['n'][0]):
            EmployFactory.create()
            PatientFactory.create()

        for _ in range(options['n'][0]):
            EmployWithBossFactory.create()
            JobPositionFactory.create()

        for _ in range(options['n'][0]):
            EmploymentFactory.create()
            BankAccountFactoryEmploy.create()
            BankAccountFactoryPatient.create()
            AppointmentFactory.create()
            FamilyDoctorFactory.create()
            DepartmentFactory.create()

        for _ in range(options['n'][0]):
            HospitalRoomFactory.create()

        for _ in range(options['n'][0]):
            ResidenceFactory.create()
