from django.db.models import query
from core.models import Appointment
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from appointments.serializers import AppointmentSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    """viewset for Appointments endpoint"""
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        viewAs = self.request.query_params.get('viewAs')
        if viewAs:
            return Appointment.objects.filter(
                doctor=self.request.user.id,
                finished=False
            )
        return Appointment.objects.all()
