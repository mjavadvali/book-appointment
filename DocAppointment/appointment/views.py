from rest_framework.generics import RetrieveAPIView,CreateAPIView, ListAPIView
from .serializers import DoctorSerializer
from .models import Doctor
from rest_framework.permissions import IsAdminUser
from rest_framework import filters


class DoctorRetrieve(RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
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
        specialization = self.request.query_params.get('specialization', None)
        if specialization:
            queryset = queryset.filter(specialization__icontains=specialization)
        return queryset

