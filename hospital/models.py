from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10 , choices=[('MALE','MALE'),('FEMALE','FEMALE')])
    age = models.IntegerField()
    diognosed = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Medicine(models.Model):
    name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=50)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
