from django.contrib import admin
from .models import DoctorSchedule, Doctor, Appointment, ReviewAppointment

admin.site.register(DoctorSchedule)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(ReviewAppointment)



