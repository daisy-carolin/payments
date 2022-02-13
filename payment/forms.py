from django import forms
from django.db.models.base import Model
from django.db.models.fields.files import ImageField
from django.forms import fields
from.models import Payment

class PaymentRegistrationForm(forms.ModelForm):
    class Meta:
        model=Payment
        fields="__all__"
    