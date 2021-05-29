from django.shortcuts import render
from .models import CapacityCertificate, CertificateAssistance, CertificateDoctor, Manipulator, Official, Person
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
    model = Person
    template_name = 'cma-carnet.html' 

#class ManipulatorView(generic.ListView):
#    model = Manipulator
#    template_name = 'manipulator.html'
#    context_object_name = 'latest_manipulator_list'
#    
#    def get_queryset(self):
#        return Person.objects.order_by('-city')[:5]

def manipulator(request, article=None):    
    certificatesDoctorList = CertificateDoctor.objects.order_by('?')
    certificatesAssistanceList = CertificateAssistance.objects.order_by('?')
    carnetList = CapacityCertificate.objects.order_by('?')
    
    return render(request, 'manipulator.html', {'medicalList': certificatesDoctorList, 'assistanceList': certificatesAssistanceList, 'carnetList':carnetList})