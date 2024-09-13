# Generated by Django 5.1.1 on 2024-09-12 15:31

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_remove_reviewappointment_appointment_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeslot', models.IntegerField(choices=[(0, '09:00 - 09:30'), (1, '10:00 - 10:30'), (2, '11:00 - 11:30'), (3, '12:00 - 12:30'), (4, '13:00 - 13:30'), (5, '14:00 - 14:30'), (6, '15:00 - 15:30'), (7, '16:00 - 16:30'), (8, '17:00 - 17:30'), (9, '17:30 - 18:00'), (10, '18:30 - 19:00'), (11, '19:30 - 20:30')])),
                ('date', models.DateField(default=datetime.date.today, help_text='YYYY-MM-DD')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='create appointment date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='update appointment date')),
                ('visited', models.BooleanField(default=False)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='docotr', to='appointment.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('doctor', 'date', 'timeslot')},
            },
        ),
    ]