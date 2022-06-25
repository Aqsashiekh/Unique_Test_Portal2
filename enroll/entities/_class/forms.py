from django import forms
from .model import class_model

class _Class(forms.ModelForm):
    class Meta:
        model = class_model
        field = ['class_name']
        exclude = ()
        widgets = {
            'class_name':forms.TextInput(attrs={'class':'form-control'}),
        }