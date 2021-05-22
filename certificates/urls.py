from django.urls import path
from certificates.views import medicalCertificate, carnet


urlpatterns = [
    path('medical-certificate/', medicalCertificate, name="medical-certificate"),
    path('cma-carnet/', carnet, name="cma-carnet"),
]
