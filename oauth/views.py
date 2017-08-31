import requests
from django.shortcuts import render, redirect

# Create your views here.
drops_url = 'https://0.0.0.0:9000'

def oauth_login(request):
    url = drops_url + '/oauth2/code/get/sluice'
    return redirect(url)

def oauth_redirect_url(request, code):
    querystring = {'grant_type':'autorization_code', 'client_id':'sluice', 'code':code, 'redirect_uri':''}
    request = requests.get(drops_url + 'oauth/access_token', query=querysting)
    access_token = request.body
    return access_token
