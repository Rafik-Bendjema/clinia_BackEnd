from django.db import models


class MedicalRecord(models.Model):
    patient = models.CharField(primary_key = True , max_length = 100 , null = False , blank = False)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True)
    chronic_diseases = models.TextField(blank=True)
    birthday = models.TextField(blank=True, null=True)
    birthday_place = models.CharField(max_length=100, blank=True)
    blood_type = models.CharField(max_length=10, blank=True)
    parents_disease = models.TextField(blank=True)
    marriage_status = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.age}"

