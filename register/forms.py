from django import forms

from .models import Microservice

'''
    form for Submit Microservice
    Parameters
    ----------
    name , url, publicKey
    ----------
'''

class Microservice_Submit_Form(forms.ModelForm):

    class Meta:
        model = Microservice
        fields = ('name', 'url', 'publicKey',)
