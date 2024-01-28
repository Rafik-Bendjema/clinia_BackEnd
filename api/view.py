from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view  
from rest_framework import status
from Record.models import MedicalRecord  
from users.models import User
from appointments.models import Appointment 
from AppRequests.models import AppRequests
from .serializers import MedicalRecordSerializer, UserSerializer , AppointmentSerializer , AppointmentRequestSerializer
from django.contrib.auth.hashers import check_password


@api_view(['GET'])
def getData(request):
    print(User.objects.all())
    users = User.objects.all()

    serializer = UserSerializer(users , many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addData(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response("error data not valid" ,  status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data)



@api_view(['POST'])
def login(request):
    # Get email and password from the request data
    email = request.data.get('email')
    password = request.data.get('pwd')

    # Check if email and password are provided
    if not email or not password:
        return Response("Both email and password are required.", status=status.HTTP_400_BAD_REQUEST)

    # Check if user with the provided email exists
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response("User does not exist.", status=status.HTTP_404_NOT_FOUND)

    # Check if the provided password is correct
    if not password == user.pwd:
        print(password)
        print(user.pwd)
        return Response("Incorrect password.", status=status.HTTP_401_UNAUTHORIZED)

    # You can add additional checks or validations here if needed

    # Return a success response
    return Response(user.role, status=status.HTTP_200_OK)


#add appointment
@api_view(["POST"])
def addAppointment(request):
    serializer = AppointmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#get appointmens 
@api_view(["POST"])
def getAppointments(request):
    parameter = request.data.get('id')

    try:
        if parameter:
            # Get appointments for a specific user
            appointments = Appointment.objects.filter(patient=parameter)
        else:
            # Get all appointments
            appointments = Appointment.objects.all()

        # Serialize appointments data
        serialized_appointments = AppointmentSerializer(appointments, many=True)

        return Response(serialized_appointments.data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


#get appointmens requests
@api_view(["POST"])
def getAppointmentsRequests(request):
    parameter = request.data.get('id')

    try:
        if parameter:
            # Get appointments for a specific user
            appointments = AppRequests.objects.filter(patient=parameter)
            

        else:
            # Get all appointments
            appointments = AppRequests.objects.all()

        # Serialize appointments data
        serialized_appointments_requests = AppointmentRequestSerializer(appointments, many=True)

        return Response(serialized_appointments_requests.data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

#add appointment request
@api_view(["POST"])
def addAppointmentRequest(request):
    print(request)
    serializer = AppointmentRequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
@api_view(["POST"])
def delelteRequest(request):
            # Deleting an appointment request
        request_id = request.data.get('id', None)
        if request_id:
            try:
                appointment_request = AppRequests.objects.get(id=request_id)
                appointment_request.delete()
                return Response({"message": "Appointment request deleted successfully."}  , status=200)
            except AppRequests.DoesNotExist:
                return Response({"error": "Appointment request not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Request ID is required for deletion."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def cancelAppointment(request):
    # Get the appointment ID from the request data
    appointment_id = request.data.get('id')

    if appointment_id is None:
        return Response({"error": "Appointment ID is required"}, status=400)

    # Retrieve the appointment instance
    appointment = get_object_or_404(Appointment, id=appointment_id)

    # Check if the appointment is already canceled or completed
    if appointment.status in ['canceled', 'completed']:
        return Response({"error": "Appointment is already canceled or completed"}, status=400)

    # Update the status to 'canceled'
    appointment.status = 'canceled'

    # Save the changes to the database
    appointment.save()

    return Response({"message": "Appointment canceled successfully"} , status=200)


@api_view(["POST"])
def doneAppointment(request):
    # Get the appointment ID from the request data
    appointment_id = request.data.get('id')

    if appointment_id is None:
        return Response({"error": "Appointment ID is required"}, status=400)

    # Retrieve the appointment instance
    appointment = get_object_or_404(Appointment, id=appointment_id)

    # Check if the appointment is already canceled or completed
    if appointment.status in ['canceled', 'completed']:
        return Response({"error": "Appointment is already canceled or completed"}, status=400)

    # Update the status to 'canceled'
    appointment.status = 'completed'

    # Save the changes to the database
    appointment.save()

    return Response({"message": "Appointment completed successfully"} , status=200)



@api_view(["POST"])
def addMedicalRecord(request):
    if request.method == "POST":
        serializer = MedicalRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def getMedicalRecords(request):
    if request.method == "POST":
        patient_id = request.data.get('id')
        if patient_id:
            medical_records = MedicalRecord.objects.filter(patient=patient_id)
        else:
            medical_records = MedicalRecord.objects.all()

        if medical_records.exists():  # Check if queryset is not empty
            serializer = MedicalRecordSerializer(medical_records, many=True)
            return Response(serializer.data , status=200)
        else:
            return Response({"message": "No medical records found"}, status=status.HTTP_404_NOT_FOUND)