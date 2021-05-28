from django.shortcuts import render
from .models import CertificateAssistance, Manipulator, Official, Person
from django.views import generic

def medicalCertificate(request):
    return render(request, "medical-certificate.html")

def carnet(request):
    return render(request, "cma-carnet.html")

class CertificateLetterView(generic.DetailView):
    model = CertificateAssistance
    context_object_name = 'certificate'
    template_name = 'certificate-letter.html'
