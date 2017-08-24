from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from register.models import Microservice
from restApi.serializers import MicroserviceSerializer
from rest_framework_jwt.settings import api_settings
import time
from datetime import datetime, timedelta
# Create your views here.



'''
    rest controller for access_token:

    Parameters
    ----------
    name: string -> name of the microservice
    ----------
    GET -> response access_token
'''
def micro_access_token(request, name):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    try:
        micro = Microservice.objects.get(name=name)
    except Microservice.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        key = api_settings.JWT_SECRET_KEY
       # payload = jwt_payload_handler(micro)
        payload =  {
            'micro_id': micro.pk,
            'micro_name': micro.name,
            'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA,
        }
        

        return HttpResponse(jwt_encode_handler(payload))

'''
    rest controller for get payload as Json

    Parameters
    ----------
    name : string -> microservice_name
'''
def micro_payload(request, name):

    try:
        micro = Microservice.objects.get(name=name)
    except Microservice.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MicroserviceSerializer(micro)
        return JsonResponse(serializer.data)

