from django.db import models
from accounts.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from datetime import date, time, datetime
import datetime as datet
from django.utils.translation import gettext_lazy as _


def user_directory_path(instance, filename):
    return f'/photo_identification/{instance.email}/{filename}'


class Doctor(models.Model):
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(unique=True, blank=False, max_length=254)
    photo_ID = models.ImageField(_("photo id"),
                                  upload_to=user_directory_path,
                                  default='/avatar.png') 
    specialty_choices = (
        ('Cardiology', 'Cardiology'),
        ('Dermatology', 'Dermatology'),
        ('Endocrinology', 'Endocrinology'),
        ('Gastroenterology', 'Gastroenterology'),
        ('Hematology', 'Hematology'),
        ('Nephrology', 'Nephrology'),
        ('Neurology', 'Neurology'),
        ('Obstetrics & Gynecology', 'Obstetrics & Gynecology'),
        ('Oncology', 'Oncology'),
        ('Ophthalmology', 'Ophthalmology'),
        ('Orthopedics', 'Orthopedics'),
        ('Otolaryngology', 'Otolaryngology'),
        ('Pediatrics', 'Pediatrics'),
        ('Psychiatry', 'Psychiatry'),
        ('Pulmonology', 'Pulmonology'),
        ('Rheumatology', 'Rheumatology'),
        ('Urology', 'Urology'),
        ('General Surgery', 'General Surgery'),
        ('Plastic Surgery', 'Plastic Surgery'),
        ('Infectious Disease', 'Infectious Disease'),
        ('General', 'General'),

    )
    specialization = models.CharField(blank=False, choices=specialty_choices, max_length=150)
    no_patients_visited = models.IntegerField(default=0)


    @property
    def average_rating(self):
        avg_rating = self.rating_doctor.aggregate(models.Avg('rating'))['rating__avg']
        return avg_rating if avg_rating else 0 
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class DoctorSchedule(models.Model):
    doctor = models.ForeignKey(Doctor, related_name="doctor_schedule", on_delete=models.CASCADE)
    date = models.DateField(help_text="YYYY-MM-DD")
    starting_time = models.TimeField(auto_now=False, auto_now_add=False)
    ending_time = models.TimeField(auto_now=False, auto_now_add=False)

    def clean(self):
        am_9 = time(9, 0, 0)
        pm_2030 = time(20, 30, 0)

        if self.ending_time <= self.starting_time:
            raise ValidationError({
                'ending_time': _('Ending time must be later than starting time.')
            })
        elif self.starting_time < am_9:
            raise ValidationError(_('The starting time cannot begin before 9 AM'))
        elif self.ending_time > pm_2030:
            raise ValidationError(_('Doctors must finish their work until 8:30 PM'))


    def __str__(self):
        return f'{self.doctor} on {self.date}'
    


class Appointment(models.Model):
    class Meta:
        unique_together = ('doctor', 'date', 'timeslot')
    
    TIMESLOT_LIST = (
        (0, '09:00 - 09:30'),
        (1, '10:00 - 10:30'),
        (2, '11:00 - 11:30'),
        (3, '12:00 - 12:30'),
        (4, '13:00 - 13:30'),
        (5, '14:00 - 14:30'),
        (6, '15:00 - 15:30'),
        (7, '16:00 - 16:30'),
        (8, '17:00 - 17:30'),
        (9, '17:30 - 18:00'),
        (10, '18:30 - 19:00'),
        (11, '19:30 - 20:30'),
    )

    patient = models.ForeignKey(User,related_name='patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,related_name='docotr', on_delete=models.CASCADE)
    timeslot = models.IntegerField(choices=TIMESLOT_LIST)
    date = models.DateField(help_text="YYYY-MM-DD", default=date.today)
    created = models.DateTimeField(auto_now_add=True, verbose_name="create appointment date")
    updated = models.DateTimeField(auto_now=True, verbose_name="update appointment date")
    visited = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        try:
            schedule = DoctorSchedule.objects.get(doctor=self.doctor, date=self.date )
        except:
            raise ValidationError('The doctor is not working in this day.')
        
        start_time_str, end_time_str = self.TIMESLOT_LIST[self.timeslot][1].split(' - ')
        selected_start_time = datetime.strptime(start_time_str, '%H:%M').time()
        selected_end_time = datetime.strptime(end_time_str, '%H:%M').time()

        schedule_start_time = schedule.starting_time
        schedule_end_time = schedule.ending_time
        print('checking time')
        print("schedule_start_time", schedule_start_time)
        print("selected_start_time", selected_start_time)
        print("selected_end_time", selected_end_time)
        print("schedule_end_time", schedule_end_time)
        

        if not (schedule_start_time <= selected_start_time and selected_end_time <= schedule_end_time):
            raise ValidationError("The selected timeslot is outside the doctor's schedule for this date.")

        
        if self.visited:
            self.doctor.no_patients_visited += 1
        return super().save(*args, **kwargs)
    
    def calculate_exact_time(self, i):
        duration = self.TIMESLOT_LIST[self.timeslot][1]  # This gets the '09:00 - 09:30' part
        start_or_end = duration.split(' - ')[i]  # Use 0 for start, 1 for end
        hour, minute = start_or_end.split(':')  # Split time into hours and minutes
        exact_time = datet.time(int(hour), int(minute))  # Create a time object
        day = self.date
        exact_datetime = datetime.combine(day, exact_time)  # Combine date and time to get datetime
        return exact_datetime


    def exact_start_time(self):
        start_time = self.calculate_exact_time(0)
        return start_time
    
    def exact_end_time(self):
        end_time = self.calculate_exact_time(0)
        return end_time
    
    
    def __str__(self):
        return f'{self.date} at {self.timeslot}'
    

class ReviewAppointment(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    feedback = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.appointment.visited:
            raise ValueError('This appointemt haven not taken place.')
        elif not self.feedback or not self.rating:
            raise ValueError('you need to submit rating or feedback')
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.appointment.patient} on {self.appointment.date} at {self.appointment.TIMESLOT_LIST[self.appointment.timeslot][1]}'