from django.urls import path
from certificates.views import medicalCertificate, carnet, certificateLetter


urlpatterns = [
    path('medical-certificate/', medicalCertificate, name="medical-certificate"),
    path('cma-carnet/', carnet, name="cma-carnet"),
    path('certificate-letter/', certificateLetter, name="certificate-letter"),
]
