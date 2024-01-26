from django.urls import path 
from . import view


urlpatterns = [
    path('' , view.getData) , 
    path("add/" , view.addData)  , 
    path("login/" , view.login) , 
    path("getAppointment/" , view.getAppointments) , 
    path("addAppointment/" , view.addAppointment)
]