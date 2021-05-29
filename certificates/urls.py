from django.urls import path
from certificates.views import manipulator
from . import views


urlpatterns = [
    path('<int:pk>/medical-certificate/', views.CertificateDoctorView.as_view(), name="medical-certificate"),
    path('<int:pk>/cma-carnet/', views.CarnetView.as_view(), name="cma-carnet"),
    path('<int:pk>/certificate-letter/', views.CertificateLetterView.as_view(), name="certificate-letter"),
    path('manipulator/', manipulator, name="manipulator"),
]
