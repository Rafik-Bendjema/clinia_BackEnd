from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('canceled', 'Canceled'),
        ('completed', 'Completed'),
    ]
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    patient = models.CharField(max_length=50 , blank = False  , null = False)
    doctor = models.CharField(max_length=50 , blank = False  , null = False)
    room = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Appointment for {self.patient.username} with Dr. {self.doctor.username} on {self.date}"