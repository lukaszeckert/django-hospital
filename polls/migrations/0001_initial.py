# Generated by Django 2.1.5 on 2019-01-14 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='HospitalStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('second_name', models.CharField(max_length=40)),
                ('boss_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='polls.HospitalStaff')),
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
        migrations.AddField(
            model_name='employment',
            name='employ',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='polls.HospitalStaff'),
        ),
        migrations.AddField(
            model_name='employment',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='polls.JobPosition'),
        ),
    ]
