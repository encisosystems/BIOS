from django.urls import path
from shop.views import shop, cart, checkout

urlpatterns = [
    path('', shop, name="shop"),
    path('cart', cart, name="cart"),
    path('checkout', checkout, name="checkout"),
]