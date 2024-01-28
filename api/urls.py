from django.urls import path 
from . import view


urlpatterns = [
    path('' , view.getData) , 
    path("add/" , view.addData)  , 
    path("login/" , view.login) , 
    path("getAppointment/" , view.getAppointments) , 
    path("addAppointment/" , view.addAppointment) , 
    path("getRequests/" , view.getAppointmentsRequests) , 
    path("addRequest" , view.addAppointmentRequest) , 
    path("cancelAppointment/"  , view.cancelAppointment) , 
    path("doneAppointment/"  , view.doneAppointment) , 
    path("getRecords/" , view.getMedicalRecords) , 
    path("addRecord/" , view.addMedicalRecord) , 
    path("deleteRequest/" , view.delelteRequest)
]