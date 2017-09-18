from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils import timezone 
from oauth.models import SluiceUser
from .forms import Microservice_Submit_Form

from .models import Microservice
import json
import requests
from sshpubkeys import SSHKey
# Create your views here.


'''
    views index
'''
def index(request):
    header = get_html_content('header')
    navigation = get_html_content('navigation')
    return render(request, 'register/index.html', {'header':  header, 'navigation': navigation})

'''
    views micro_add

    use add_microservice.html 
    use Microservice_Submit_Form

    adds a Microservice over Formular
'''
def add_microservice(request):
    if request.session.has_key('pool_id'):
        try:
            user =  SluiceUser.objects.get(pk=request.session['pool_id'])
        except SluiceUser.DoesNotExist as error:
            BadRequest(error)
        if request.method == 'POST':
            form = Microservice_Submit_Form(request.POST)
            if form.is_valid():
                micro = form.save(commit=False)
                micro.owner = user
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
        #return top + '\n' + str(bottom)
    else:
        return HttpResponseRedirect('../../oauth/login')
'''
    list all Microservices
'''
def list_microservice(request):
    if request.session.has_key('pool_id'):
        user = SluiceUser.objects.get(pk=request.session['pool_id'])
        microservices_list = list(Microservice.objects.filter(owner=user))   #filter(modifyed_date__lte=timezone.now()).order_by('modifyed_date')
        return render(request, 'register/list_microservice.html', {'microservices': microservices_list})
        #return top + '\n' + bottom
    else:
        return HttpResponseRedirect('../../oauth/login')

def get_html_content(jsonName):
    fullJsonPath = 'json/' + jsonName + '.txt'
    with open(fullJsonPath) as json_file:
        templateJson = json.load(json_file)
        req = requests.post('http://172.17.0.1:4000/getTemplate', json=templateJson)
        print(req.text)
    return req.text

