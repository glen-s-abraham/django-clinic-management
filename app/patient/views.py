from core.models import Patient
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from patient.serializers import PatientSerializer
# Create your views here.


class PatientViewSet(viewsets.ModelViewSet):
    """View for Patients endpoint"""
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
