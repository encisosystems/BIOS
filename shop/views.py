from django.shortcuts import render

# Create your views here.
def shop(request):
    context={}
    return render (request, 'shop.html')

def cart(request):
    context={}
    return render (request, 'cart.html', context)

def checkout(request):
    context={}
    return render (request, 'checkout.html', context)