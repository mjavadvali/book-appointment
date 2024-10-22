from celery import shared_task
from django.core.mail import send_mail
from .models import Appointment
from datetime import timedelta
from django.utils import timezone
from django.core.mail import send_mail


@shared_task
def appointment_notif():
    now = timezone.now()
    near_appointments_11_30 = now + timedelta(hours=11, minutes=45)
    near_appointments_12 = now + timedelta(hours=12)
    near_appoitments = Appointment.objects.filter(
        exact_start_time__gte=near_appointments_11_30,
        exact_start_time__lte=near_appointments_12
    )

    for appointment in near_appoitments:

        start_time = appointment.exact_start_time()
        hour = start_time.hour
        minute = start_time.minute

        subject = "Upcoming Appointment Reminder"
        message = (
            f"Dear {appointment.patient.username},\n\n"
            f"This is a reminder for your upcoming appointment with Dr. {appointment.doctor.username} "
            f"on {appointment.date} at {hour}:{minute} .\n\n"
            f"Please ensure to arrive on time.\n\n"
            f"Thank you,\nYour Health Team"
        )

    recipient_list = [appointment.patient.email]

    send_mail(subject, message, 'no-reply@example.com', recipient_list)

    