
from secrets import choice
from tkinter import Widget
from django import forms
from django.forms import ModelForm
from .models import Profile


STATE = [
    ('Abia', 'Abia'),
    ('Edo', 'Edo'),
    ('Lagos', 'Lagos'),
    ('Bayelsa', 'Bayelsa')
]
class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [ 'first_name','last_name', 'email', 'phone', 'address','city', 'state', 'profile_pix']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name is required'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name is required'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email is required'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address is required'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'city is required'}),
            'state': forms.Select(attrs={'class': 'form-control', 'placeholder': 'state is required'}, choices=STATE),
            "profile_pix": forms.FileInput(attrs ={'class': 'form-control'}),
        }
