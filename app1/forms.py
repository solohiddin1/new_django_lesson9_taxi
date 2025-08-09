from django import forms
from .models import Client, Driver, Tarif, Deal, Comment



class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'number', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['name', 'phone_number', 'email', 'vehicle_model', 'license_plate', 'sum_km']

class TarifForm(forms.ModelForm):
    class Meta:
        model = Tarif
        fields = ['title', 'karra']

class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ['client', 'driver', 'from_where', 'to_where', 'tarif', 'distance', 'total_cost', 'rate']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ['deal', 'client', 'text']