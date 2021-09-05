from rest_framework import serializers
from core.models import Diagnosis


class DiagnosisSerializer(serializers.ModelSerializer):
    """Serializer for Diagnosis model"""
    class Meta:
        model = Diagnosis
        fields = '__all__'
        read_only_fields = ('id',)
