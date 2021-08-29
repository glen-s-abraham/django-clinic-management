from rest_framework import viewsets
from core.models import Prescription
from prescription.serializers import PrescriptionSerializer


class PrescriptionViewSet(viewsets.ModelViewSet):
    """View set from Prescriptions"""
    serializer_class = PrescriptionSerializer
    queryset = Prescription.objects.all()


"""
TODO
    1.add authentication
    2.custom creation to add logged in user before submissions
"""
