from django.urls import path
from certificates.views import medicalCertificate


urlpatterns = [
    path('medical-certificate/', medicalCertificate, name="medical-certificate"),
]
