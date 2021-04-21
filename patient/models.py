from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Patient(models.Model):
    
    first_name   = models.CharField(max_length=20)
    last_name    =models.CharField(max_length=30)
    street       =models.CharField(max_length=30)
    city         =models.CharField(max_length=30,default="Tychy")
    number       =models.PositiveIntegerField()
    phone_number =models.CharField(max_length=30)
    

    def get_absolute_url(self):
         return reverse("patient:patient-detail",kwargs={"id":self.id})