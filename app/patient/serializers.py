from rest_framework import serializers
from core.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    """Serializer fot Patients"""
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ('id',)
