import sys
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
#from sshpubkeys import SSHKey
#import pem
#import sshpubkeys
from Crypto.PublicKey import RSA

# Create your models here.

'''
    Microservice Model

    Parameters
    ----------
    name : string
    url : string
    publicKey : string
    created_date : time
    modifyed_date : time
'''

def validate_ssh_key(value):
    #validate = SSHKey(value)
    try:
        publicKeyObject = RSA.importKey(value)
    #except SSHKey.InvalidKeyError as err:
    #    raise ValidationError(_('Invalid Key: ' + err))
    except Exception as err:
        raise ValidationError(_('Invalid Key Typ'))

class Microservice(models.Model):
    #owner = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200, primary_key=True)
    url = models.CharField(max_length=200)
    publicKey = models.TextField(validators=[validate_ssh_key])
    created_date = models.DateTimeField(
            default=timezone.now)
    modifyed_date = models.DateTimeField(
            blank=True, null=True)

    def register(self):
        self.modifyed_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.name

