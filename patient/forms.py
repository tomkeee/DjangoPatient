from django import forms
from .models import Patient
from django.forms import ModelForm

class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields=["first_name","last_name","street","city","number","phone_number"]

        widgets ={
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'street': forms.TextInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'number': forms.NumberInput(attrs={'class':'form-control'}),
            'phone_number': forms.TextInput(attrs={'class':'form-control'}),

        } 
