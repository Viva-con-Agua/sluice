from django.shortcuts import render, redirect

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils import timezone 
 

from .forms import MicroserviceForm

from .models import Microservice
# Create your views here.

def index(request):
    return render(request, 'register/index.html', {})

def add_microservice(request):
    if request.method == 'POST':
        form = MicroserviceForm(request.POST)
        if form.is_valid():
            micro = form.save(commit=False)
           # micro.name = request.name
           # micro.url = request.url
           # micro.publicKey = request.publicKey
            micro.created_date = timezone.now()
            micro.modifyed_date = micro.created_date
            micro.save()
            return redirect('add_microservice')
    else:    
        form = MicroserviceForm()
    return render(request, 'register/add_microservice.html', {'form': form})

def list_microservice(request):
    microservices = Microservice.objects
    return render(request, 'register/list_microservice.html', {'microservices': microservices})

    
