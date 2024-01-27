from rest_framework import serializers
from users.models import User
from appointments.models import Appointment 
from AppRequests.models import AppRequests
from Record.models import MedicalRecord
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppRequests
        fields = '__all__'



class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'
