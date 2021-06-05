from django.http import HttpResponse
from django.shortcuts import render
from cms.models import *

def home(request):
    images = Image.objects.all()
    context={'images':images}
    return render (request, 'home.html', context) 