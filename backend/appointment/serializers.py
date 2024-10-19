from rest_framework import serializers
from .models import Doctor, Appointment, DoctorSchedule, ReviewAppointment

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ["id" ,"first_name", 
                  "last_name", "email",
                   "specialization", 
                   "photo_ID"
                  ]
        

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['patient','doctor' ,"date", "timeslot"]
        
       
        def validate(self, data):
            today = date.today()

            doctor = data['doctor']
            date = data['date']
            timeslot = data['timeslot']


            if date < today:
                raise serializers.ValidationError("You can not select passed days.")
            elif Appointment.objects.filter(doctor=doctor, date=date, timeslot=timeslot).exists():
                raise serializers.ValidationError("This doctor is already booked for this timeslot on the selected date.")




class DoctorScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorSchedule
        fields = "__all__"

    
class ReviewAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewAppointment
        fields = '__all__'

    def validate(self, data):
        appointment = data['appointment']
        
        if not appointment.visited : 
            raise serializers.ValidationError('you didn\'t visit the doctor.')
        
        return data