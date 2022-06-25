from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        field = ['user_name', 'password', 'user_type', 'class_id','phone_number', 'email', 'addresss']
        exclude = ()
        widgets = {
            'user_name':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
            'user_type':forms.TextInput(attrs={'class':'form-control'}),
            'class_id':forms.TextInput(attrs={'class':'form-control'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
        }
