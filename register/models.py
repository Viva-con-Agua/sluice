from django.db import models
from django.utils import timezone
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

class Microservice(models.Model):
    #owner = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200, primary_key=True)
    url = models.CharField(max_length=200)
    publicKey = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    modifyed_date = models.DateTimeField(
            blank=True, null=True)

    def register(self):
        self.modifyed_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.name

