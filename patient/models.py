from django.db import models

# Create your models here.

class PatientData(models.Model):


    def __str__(self):
        return self.patient_name

    patient_name = models.CharField(max_length=200)
    patient_code = models.CharField(max_length=200)
    patient_age = models.IntegerField(default=0)
    physician_name = models.CharField(max_length=200)
    diagnostics = models.TextField(default='Nothing')

    patient_picture = models.ImageField(upload_to='uploads/')