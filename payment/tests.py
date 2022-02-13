from django.test import TestCase

# Create your tests here.
from.views import edit_payment, register_payment, payment_profile
from django.urls import path
from.views import register_payment,payment_list
from.views import payment_profile
from django.urls import reverse



urlpatterns = [
    path("register/",register_payment,name="register_payment"),
    path("list/",payment_list,name="payment_list"),
    path("profile/<int:id>/",payment_profile,name="payment_profile"),
    path("edit/<int:id>/",edit_payment,name="edit_payment"),

    
]
