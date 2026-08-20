from django import forms
from . import models
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['bio', 'contact', 'location']
        widgets = {
            'bio': forms.Textarea(attrs={'rows':3})
        }


class EditProfileForm1(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields.values():
            field.help_text = None
    
