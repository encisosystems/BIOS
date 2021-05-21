from django.http import HttpResponse
from django.shortcuts import render

def blog(request):
    return render(request, "blog.html")

def blogDetails(request):
    return render(request, "blog-details.html")
