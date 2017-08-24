from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from register.models import Microservice
from restApi.serializers import MicroserviceSerializer
# Create your views here.

def micro_payload(request, name):

    try:
        micro = Microservice.objects.get(name=name)
    except Microservice.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MicroserviceSerializer(micro)
        return JsonResponse(serializer.data)

