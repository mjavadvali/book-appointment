# Generated by Django 5.1.1 on 2024-09-24 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0006_doctorschedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewappointment',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='reviewappointment',
            name='patient',
        ),
    ]
