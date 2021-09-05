from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from core.models import Diagnosis
from diagnosis.serializers import DiagnosisSerializer


class DiagnosisViewSet(viewsets.ModelViewSet):
    """View set for Diagnosis"""
    serializer_class = DiagnosisSerializer
    queryset = Diagnosis.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        """create new diagnosis"""
        serializer.save(doctor=self.request.user)

    def get_queryset(self):
        return Diagnosis.objects.filter(doctor=self.request.user.id)
