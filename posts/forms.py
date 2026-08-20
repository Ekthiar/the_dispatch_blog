from django import forms
from . import models


class PostForm(forms.ModelForm):

    class Meta:
        model = models.Post
        fields = ["title","content","cetagory","image"]

        widgets = {
            "content": forms.Textarea(
                attrs={
                    "rows": 5
                }
            ),

            "cetagory": forms.CheckboxSelectMultiple(
                attrs={
                    "class": "form-check-input"
                }
            ),
        }

