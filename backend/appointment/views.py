from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    ListAPIView, 
    RetrieveAPIView)
from .serializers import (
    DoctorSerializer,
    AppointmentSerializer, 
    DoctorScheduleSerializer,
    ReviewAppointmentSerializer)
from .models import (
    Doctor, 
    Appointment, 
    DoctorSchedule,
    ReviewAppointment)
from rest_framework.permissions import IsAdminUser
from rest_framework import filters, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.db.models import Q


class DoctorRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    # permission_classes = [permissions.IsAdminorOwner]
    lookup_field = 'id'

class CreateDoctor(CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAdminUser]


class DoctorsListView(ListAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['specialization']

    def get_queryset(self):
        queryset = super().get_queryset()
        speciality = self.kwargs.get('speciality', None)
        if speciality:
            queryset = queryset.filter(specialization__icontains=speciality)
        return queryset

class BookingAppointment(CreateAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    # permission_classes = []
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data= request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewAppointmentView(CreateAPIView):
    serializer_class = ReviewAppointmentSerializer
    queryset = ReviewAppointment.objects.all()
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data= request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("Validation errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class AddDoctorSchedule(CreateAPIView):
    permission_classes = [IsAdminUser,]
    serializer_class = DoctorScheduleSerializer
    queryset = DoctorSchedule.objects.all()


class Patientprofile(RetrieveAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

    # permission_classes

    def get_queryset(self):
        qs = super().get_queryset() 
        qs.filter(user=self.request.user)
        return qs
    

# class ReviewAppointmentView(CreateAPIView):
#     serializer_class = ReviewAppointmentSerializer
#     queryset = ReviewAppointment.objects.all()


@api_view(["GET"])
def get_specialty_choices(request):
    specialty_choices = Doctor.specialty_choices
    specialty_choices = [spc[0] for spc in specialty_choices]
    return Response(specialty_choices)

@api_view(['GET'])
def get_empty_time_slots(request):
    doctor_id = request.query_params.get('doctor_id')
    date = request.query_params.get('date')

    time_slots = [timeslot[1] for timeslot in Appointment.TIMESLOT_LIST] 
    

    doctor = get_object_or_404(Doctor, pk=int(doctor_id))
    doctor_schedule_day = get_object_or_404(DoctorSchedule, doctor=doctor, date=date)

    start_time = doctor_schedule_day.starting_time
    end_time = doctor_schedule_day.ending_time

    time_slots = [(index, slot) for index, slot in Appointment.TIMESLOT_LIST]

    available_slots = []
    for index, slot in time_slots:
        slot_start_time_str = slot.split(' - ')[0]
        slot_start_time = datetime.strptime(slot_start_time_str, '%H:%M').time()

        if start_time <= slot_start_time < end_time:
            available_slots.append(slot)

    booked_appointments = Appointment.objects.filter(doctor=doctor, date=date)
    booked_timeslots = booked_appointments.values_list('timeslot', flat=True)

    final_available_slots = [
        (index, slot) for index, slot in time_slots 
        if index not in booked_timeslots and slot in available_slots
    ]

    return Response({'available_slots': final_available_slots})


@api_view(['post'])
def send_review_appointment(request):
    score = request.data.get('score')
    feedback = request.data.get('feedback')
    appointment_pk = request.data.get('appointment')

    appointment = get_object_or_404(Appointment, pk=appointment_pk)

    appointment_review = ReviewAppointment(appointment=appointment, rating=score, feedback=feedback)
    appointment_review.save()

    return Response({'message': 'the appointment review is send'})

@api_view(['GET'])
def search_view(request):
    query = request.query_params.get('q')
    print(query)
    if query:
        if ' ' in query and query.count(' ') == 1:
            first, last = query.split(' ')[0], query.split(' ')[1]
            print(first, last)
            doctors = Doctor.objects.filter(
                Q(first_name__istartswith=first) | Q(last_name__istartswith=last)
            )
        else:
            doctors = Doctor.objects.filter(
                Q(first_name__istartswith=query) | Q(last_name__istartswith=query)
            )
        data = [{'name': f"{doctor.first_name} {doctor.last_name}", 'pk': doctor.pk} for doctor in doctors]
    else:
        data = [] 
   
    return Response(data)



@api_view(['GET'])
def check_app_reviewed(request):
    appointment_id = request.query_params.get('id')
    
    if appointment_id is None:
        return Response({'error': 'Appointment ID is required.'}, status=status.HTTP_400_BAD_REQUEST)

    appointment = get_object_or_404(Appointment, pk=appointment_id)

    is_appointment_reviewed = ReviewAppointment.objects.filter(appointment=appointment).exists()

    return Response({'is_reviewed': is_appointment_reviewed}) 