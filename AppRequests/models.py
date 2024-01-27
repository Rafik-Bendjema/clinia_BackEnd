from django.db import models

class AppRequests(models.Model) : 
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    patient = models.CharField(max_length=50 , blank = False  , null = False)
    
    def __str__(self):
        return f"{self.date}"
