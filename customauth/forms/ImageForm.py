from django import forms
from customauth.models import  Image

class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['name', 'image']