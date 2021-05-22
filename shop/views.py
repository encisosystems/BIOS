from django.shortcuts import render
from .models import *
# Create your views here.
def shop(request):
    products = Product.objects.all()
    context={'products':products}
    return render (request, 'shop.html',context)

def cart(request):
    context={}
    return render (request, 'cart.html', context)

def checkout(request):
    context={}
    return render (request, 'checkout.html', context)
