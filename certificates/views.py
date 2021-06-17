from django.http import request, response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms import Form
from .models import CapacityCertificate, CertificateAssistance, CertificateDoctor, ConcepType, Person, Test
from django.views import generic

#class CertificateDoctorView(generic.DetailView):
#    model = CertificateDoctor
#    context_object_name = 'certificate'
#    template_name = 'medical-certificate.html'

class CertificateLetterView(generic.DetailView):
    model = CertificateAssistance
    context_object_name = 'certificate'
    template_name = 'certificate-letter.html'

def certificateDoctor(request,certificate_id):
    certificate = CertificateDoctor.objects.get(pk=certificate_id)
    tests = Test.objects.filter(certificate_id=certificate_id)
    concepts = ConcepType.objects.all()
    return render(request, 'medical-certificate.html', {'certificate': certificate, 'tests': tests, 'concepts':concepts})

class CarnetView(generic.DetailView):
    model = CapacityCertificate
    context_object_name = 'capacity'
    template_name = 'cma-carnet.html'

def manipulator(request):    
    certificatesDoctorList = CertificateDoctor.objects.order_by()
    certificatesAssistanceList = CertificateAssistance.objects.order_by()
    carnetList = CapacityCertificate.objects.order_by()
    if request.method == "POST":
        searched  = request.POST['searched']
        cc_id = Person.objects.filter(identification__contains=searched)
        return render(request, 'manipulator.html',{'cc_id':cc_id,'searched':searched,'medicalList': certificatesDoctorList, 'assistanceList': certificatesAssistanceList, 'carnetList':carnetList})
    else:
        return render(request, 'manipulator.html', {})

    #return render(request, 'manipulator.html', {'object':obj,'medicalList': certificatesDoctorList, 'assistanceList': certificatesAssistanceList, 'carnetList':carnetList})
