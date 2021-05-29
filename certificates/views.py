from django.shortcuts import render
from .models import CapacityCertificate, CertificateAssistance, CertificateDoctor
from django.views import generic

class CertificateDoctorView(generic.DetailView):
    model = CertificateDoctor
    context_object_name = 'certificate'
    template_name = 'medical-certificate.html'

class CertificateLetterView(generic.DetailView):
    model = CertificateAssistance
    context_object_name = 'certificate'
    template_name = 'certificate-letter.html'

class CarnetView(generic.DetailView):
    model = CapacityCertificate
    context_object_name = 'capacity'
    template_name = 'cma-carnet.html' 

def manipulator(request, article=None):    
    certificatesDoctorList = CertificateDoctor.objects.order_by()
    certificatesAssistanceList = CertificateAssistance.objects.order_by()
    carnetList = CapacityCertificate.objects.order_by()
    
    return render(request, 'manipulator.html', {'medicalList': certificatesDoctorList, 'assistanceList': certificatesAssistanceList, 'carnetList':carnetList})