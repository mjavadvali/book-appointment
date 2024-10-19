from django.test import TestCase
from django.core.exceptions import ValidationError
from datetime import datetime, date, time
from .models import Appointment, DoctorSchedule, Doctor
from accounts.models import User

class AppointmentModelTest(TestCase):
    def setUp(self):
        # Create a doctor
        self.doctor = Doctor.objects.create(email="DrSmith@gmail.com")
        
        self.patient = User.objects.create(username='john_doe')

        self.schedule = DoctorSchedule.objects.create(
            doctor=self.doctor,
            date=date.today(),
            starting_time=datetime.strptime('09:00', '%H:%M'),
            ending_time=datetime.strptime('17:30', '%H:%M')
        )

    def test_create_valid_appointment(self):
        appointment = Appointment.objects.create(
            patient=self.patient,
            doctor=self.doctor,
            timeslot=0,  # '09:00 - 09:30'
            date=date.today()
        )
        self.assertEqual(Appointment.objects.count(), 1)
        self.assertEqual(appointment.timeslot, 0)

    def test_create_appointment_outside_schedule(self):
        appointment = Appointment(
            patient=self.patient,
            doctor=self.doctor,
            timeslot=11,  # '19:30 - 20:30', outside working hours
            date=date.today()
        )
        with self.assertRaises(ValidationError):
            appointment.save()

    def test_create_appointment_on_non_working_day(self):
        different_day = date(2024, 9, 25)
        appointment = Appointment(
            patient=self.patient,
            doctor=self.doctor,
            timeslot=0,  # '09:00 - 09:30'
            date=different_day
        )
        with self.assertRaises(ValidationError):
            appointment.save()

    def test_unique_appointment(self):
        appointment1 = Appointment.objects.create(
            patient=self.patient,
            doctor=self.doctor,
            timeslot=0,  # '09:00 - 09:30'
            date=date.today()
        )
        appointment2 = Appointment(
            patient=self.patient,
            doctor=self.doctor,
            timeslot=0,  # '09:00 - 09:30'
            date=date.today()
        )
        with self.assertRaises(ValidationError):
            appointment2.save()

    def test_doctor_patient_visit_increases_count(self):
        # Create a valid appointment and mark it as visited
        appointment = Appointment.objects.create(
            patient=self.patient,
            doctor=self.doctor,
            timeslot=0,  # '09:00 - 09:30'
            date=date.today(),
            visited=True
        )
        # Check if the doctor's no_patients_visited count increases
        self.doctor.refresh_from_db()
        self.assertEqual(self.doctor.no_patients_visited, 1)

    def test_exact_times(self):
        # Create a valid appointment
        appointment = Appointment.objects.create(
            patient=self.patient,
            doctor=self.doctor,
            timeslot=0,  # '09:00 - 09:30'
            date=date.today()
        )
        # Check if the exact start time is calculated correctly
        self.assertEqual(appointment.exact_start_time().time(), datetime.strptime('09:00', '%H:%M').time())
        # Check if the exact end time is calculated correctly
        self.assertEqual(appointment.exact_end_time().time(), datetime.strptime('09:30', '%H:%M').time())
