from django.db import models

# Create your models here.
class PatientReg(models.Model):
    pname = models.CharField(max_length=100)
    pemail = models.CharField(max_length=100)
    pphone = models.CharField(max_length=100)
    paddress = models.TextField()
    password = models.CharField(max_length=100)
    report= models.CharField(max_length=100)
    reportof= models.CharField(max_length=100)
    doctornm= models.CharField(max_length=100)