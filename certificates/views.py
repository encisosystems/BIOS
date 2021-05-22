from django.shortcuts import render

def medicalCertificate(request):
    return render(request, "medical-certificate.html")
