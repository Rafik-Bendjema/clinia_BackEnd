from rest_framework.response import Response
from rest_framework.decorators import api_view  
from rest_framework import status  
from users.models import User
from appointments.models import Appointment
from .serializers import UserSerializer , AppointmentSerializer

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

from django.contrib.auth.hashers import check_password

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
    return Response("Login successful!", status=status.HTTP_200_OK)


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