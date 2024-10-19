from django.urls import path
from . import views


urlpatterns = [
    path('doctor/<int:id>/', views.DoctorRetrieve.as_view(), name='docotr_detail'),
    path('doctor/create_doctor/', views.CreateDoctor.as_view(), name='create_doctor_profile'),
    path('doctor/add_schedule/', views.AddDoctorSchedule.as_view(), name='add-schedule'),
    path('doctors/', views.DoctorsListView.as_view(), name='doctor-list'),
    path('doctors/<str:speciality>/', views.DoctorsListView.as_view(), name='doctors-by-specialization'),

    path('appointment/booking/', views.BookingAppointment.as_view(), name='book-appointment'),
    path('api/get_empty_time_slots/', views.get_empty_time_slots, name='get_empty_time_slots'),
    
    path('patient/profile/', views.Patientprofile.as_view(), name='patient-profile'),
    path('appointment/review/', views.ReviewAppointmentView.as_view(), name='send_review_appointment'),
    

    path('api/specialty_choices/', views.get_specialty_choices, name='specialty-choices'),
    path('api/search_view/', views.search_view, name='search_view'),
    path('api/check_app_reviewed/', views.check_app_reviewed, name='check_app_reviewed'),

    
]
