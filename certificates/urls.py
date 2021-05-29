from django.urls import path
from certificates.views import medicalCertificate, carnet
from . import views


urlpatterns = [
    path('medical-certificate/', medicalCertificate, name="medical-certificate"),
    path('<int:pk>/cma-carnet/', views.CarnetView.as_view(), name="cma-carnet"),
    path('<int:pk>/certificate-letter/', views.CertificateLetterView.as_view(), name="certificate-letter"),
    path('manipulator/', views.ManipulatorView.as_view(), name="manipulator"),
]
