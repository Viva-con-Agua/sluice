from django import forms

from .models import Microservice

class MicroserviceForm(forms.ModelForm):

    class Meta:
        model = Microservice
        fields = ('name', 'url', 'publicKey',)
