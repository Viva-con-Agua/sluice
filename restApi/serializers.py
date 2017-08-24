from rest_framework import serializers
from register.models import Microservice



'''
    serializer Microservice Model for REST
    fields are used Variables
'''
class MicroserviceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Microservice
        fields = ('name', 'url', 'publicKey', 'created_date', 'modifyed_date') 

