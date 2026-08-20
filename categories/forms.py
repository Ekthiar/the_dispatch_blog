from django import forms
from . import models

class CetagoryForm(forms.ModelForm):
    class Meta:
        model = models.Cetagory
        fields = '__all__'
        
        