from rest_framework import serializers
from core.models import Prescription


class PrescriptionSerializer(serializers.ModelSerializer):
    """Serializer for prescreptions"""
    class Meta:
        model = Prescription
        fields = '__all__'
        read_only_fields = ('id',)
