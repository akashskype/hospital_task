from django.contrib import admin
from .models import Doctor, Patient, Medicine

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'specialization', 'phone_number')

class PatientAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'gender', 'age', 'phone_number','diognosed')

class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'dosage', 'patient', 'doctor')

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Medicine, MedicineAdmin)
