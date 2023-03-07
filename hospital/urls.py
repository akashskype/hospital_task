from django.urls import path
from .views import DoctorList, DoctorDetail, PatientList, PatientDetail, MedicineList, MedicineDetail

urlpatterns = [
    path('doctors/', DoctorList.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', DoctorDetail.as_view(), name='doctor-detail'),
    path('patients/', PatientList.as_view(), name='patient-list'),
    path('patients/<int:pk>/', PatientDetail.as_view(), name='patient-detail'),
    path('medicines/', MedicineList.as_view(), name='medicine-list'),
    path('medicines/<int:pk>/', MedicineDetail.as_view(), name='medicine-detail'),
]
