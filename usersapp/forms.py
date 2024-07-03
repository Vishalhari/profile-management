from django import forms
from .models import Users


class Userform(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name','email','password','confirm_password','usertype']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Full Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Full Name'}),
            'confirm_password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Full Name'}),
            'usertype': forms.HiddenInput(attrs={'value':'user'})
        }

