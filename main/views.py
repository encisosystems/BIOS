from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('<h1>We are developing this site!</h1>'
                        '<div>Project developed by <a href="https://www.encisosystems.com/" target="_blank">Enciso Systems</a>.</div>')
