from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from core.models import Prescription
from prescription.serializers import PrescriptionSerializer


class PrescriptionViewSet(viewsets.ModelViewSet):
    """View set from Prescriptions"""
    serializer_class = PrescriptionSerializer
    queryset = Prescription.objects.filter()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        """create a new prescription"""
        serializer.save(doctor=self.request.user)
