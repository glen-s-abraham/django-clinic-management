from rest_framework import serializers
from core.models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    """Serializer for Appointments"""
    class Meta:
        model = Appointment
        fields = '__all__'
        read_only_fields = ('id',)
