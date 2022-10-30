""" cart app urls file """
from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('add/<event_id>', views.add_to_cart, name='add_to_cart'),
]
