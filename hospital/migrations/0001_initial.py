# Generated by Django 2.1.3 on 2019-01-20 11:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=30)),
                ('number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Employ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('second_name', models.CharField(max_length=40)),
                ('boss', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='hospital.Employ')),
            ],
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.FloatField()),
                ('employ', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hospital.Employ')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyDoctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('employ', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hospital.Employ')),
            ],
        ),
        migrations.CreateModel(
            name='HospitalRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('places', models.IntegerField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hospital.Department')),
            ],
        ),
        migrations.CreateModel(
            name='JobPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('base_salary', models.IntegerField()),
                ('number_hours', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField()),
                ('first_name', models.CharField(max_length=30)),
                ('second_name', models.CharField(max_length=30)),
                ('personal_number', models.CharField(max_length=11)),
                ('nfz_number', models.CharField(blank=True, default=None, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Residence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beginning_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hospital.Patient')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hospital.HospitalRoom')),
            ],
        ),
        migrations.AddField(
            model_name='familydoctor',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hospital.Patient'),
        ),
        migrations.AddField(
            model_name='employment',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hospital.JobPosition'),
        ),
        migrations.AddField(
            model_name='department',
            name='chief',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hospital.Employ'),
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='employ',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='hospital.Employ'),
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='hospital.Patient'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='employ',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hospital.Employ'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hospital.Patient'),
        ),
    ]
