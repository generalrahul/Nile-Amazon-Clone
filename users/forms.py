from django import forms
from .models import CustomUser

class SellerRegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'is_seller']  # Add seller-specific fields

class BuyerRegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']  # Add buyer-specific fields
