from django.urls import path
from certificates.views import certificateDoctor, manipulator
from . import views


urlpatterns = [
    path('<int:certificate_id>/medical-certificate/', certificateDoctor, name="medical-certificate"),
    path('<int:pk>/cma-carnet/', views.CarnetView.as_view(), name="cma-carnet"),
    path('<int:pk>/certificate-letter/', views.CertificateLetterView.as_view(), name="certificate-letter"),
    path('manipulator/', manipulator, name="manipulator"),
]
