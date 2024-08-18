from django import forms
from authers.models import Auther

class Autherform(forms.ModelForm):
    class Meta:
        model = Auther
        fields ='__all__'

        
