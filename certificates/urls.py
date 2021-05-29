from django.urls import path
from certificates.views import manipulator, medicalCertificate
from . import views


urlpatterns = [
    path('medical-certificate/', medicalCertificate, name="medical-certificate"),
    path('<int:pk>/cma-carnet/', views.CarnetView.as_view(), name="cma-carnet"),
    path('<int:pk>/certificate-letter/', views.CertificateLetterView.as_view(), name="certificate-letter"),
    path('manipulator/', manipulator, name="manipulator"),
]
