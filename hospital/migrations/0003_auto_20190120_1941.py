# Generated by Django 2.1.3 on 2019-01-20 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_auto_20190120_1752'),
    ]

    operations = [
        migrations.RunSQL(
        """
        CREATE FUNCTION raise_salary(percent float) RETURNS void
        AS $$
        UPDATE hospital_jobposition SET base_salary = ((1 + percent / 100) * base_salary)::numeric::integer; 
        $$ LANGUAGE SQL;
        """,
        """
        DROP FUNCTION raise_salary(float);
        """)
    ]