from django.shortcuts import render, redirect

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils import timezone 
 

from .forms import Microservice_Submit_Form

from .models import Microservice
# Create your views here.


'''
    views index
'''
def index(request):
    return render(request, 'register/index.html', {})

'''
    views micro_add

    use add_microservice.html 
    use Microservice_Submit_Form

    adds a Microservice over Formular
'''
def add_microservice(request):
    if request.method == 'POST':
        form = Microservice_Submit_Form(request.POST)
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
        form = Microservice_Submit_Form()
    return render(request, 'register/add_microservice.html', {'form': form})

'''
    list all Microservices
'''
def list_microservice(request):
    microservices = Microservice.objects
    return render(request, 'register/list_microservice.html', {'microservices': microservices})

    
