from rest_framework.permissions import AllowAny
from rest_framework import generics, response, status
from .serializers import UserProfileCreateSerializer
from rest_framework.generics import RetrieveAPIView
from django.contrib.auth import login
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import User
from rest_framework.response import Response
from appointment.models import Appointment, Doctor
from appointment.serializers import AppointmentSerializer

from django.http.response import JsonResponse


class UserSignUpView(generics.GenericAPIView):
    serializer_class   = UserProfileCreateSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            data = request.data
            serializer = UserProfileCreateSerializer(data = data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                login(request, user)
                
                return response.Response({
                    'status':200,
                    'message':'registered succesfully check email',
                    'data':serializer.data,
                })
            
            return response.Response({
                'status':400,
                'message':'something went wrong',
                'data': serializer.errors
            })
        
        except Exception as e:
            return response.Response({'message': f"{e}"}, status=status.HTTP_400_BAD_REQUEST)
        




@api_view(['get'])
def get_user_pk(request):
    username = request.query_params.get('username')
    user = get_object_or_404(User, username=username)
    pk = user.pk
    return Response(pk)

@api_view(['get'])
def get_user_info(request):
    user_pk = request.query_params.get('user_pk')
    user = get_object_or_404(User, pk=user_pk)
    appointments = Appointment.objects.filter(patient= user)

    appointments_list = []
    for appointment in appointments:
        dic = { 
            'id': appointment.id,
            'doctor': {
            'first_name': appointment.doctor.first_name,
            'last_name': appointment.doctor.last_name
        },
            'date': appointment.date,
               'visited': appointment.visited, 'time' : appointment.TIMESLOT_LIST[appointment.timeslot][1]}
        
        appointments_list.append(dic)
    user_info_list = [{'username': user.username, 'email': user.email, 'created': user.created}]

    return JsonResponse({'appointments': appointments_list,
                         'user_info': user_info_list
                    })


@api_view(['POST'])
def reset_email(request):
    username = request.data.get('username')
    new_email = request.data.get('newEmail')

    user = get_object_or_404(User, username= username)
    user.email = new_email
    user.save()

    return Response({'message': 'the new email is received', 'email': new_email})