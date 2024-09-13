from django.urls import path
from . import views


urlpatterns = [
    path('doctor/<int:id>/', views.DoctorRetrieve.as_view(), name='docotr_detaik'),
    path('doctor/create_doctor/', views.CreateDoctor.as_view(), name='create_doctor_profile'),
    path('doctors/', views.DoctorsListView.as_view(), name='doctor-list'),
]
