from django.shortcuts import render

def medicalCertificate(request):
    return render(request, "medical-certificate.html")

def carnet(request):
    return render(request, "cma-carnet.html")

def certificateLetter(request):
    return render(request, "certificate-letter.html")
