from django.db import models

class User(models.Model):
    ROLE_CHOICES = [
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    ]

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    second_name = models.CharField(max_length=255, blank=False, null=True)
    email = models.CharField(max_length=255, blank=False, null=False, default="def@email.com")
    pwd = models.CharField(max_length=255, blank=False, null=False, default="pass")
    age = models.IntegerField()
    pic = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='patient')

    def __str__(self):
        return f'{self.first_name} {self.second_name}' if self.second_name else f'{self.first_name}'
