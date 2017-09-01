import requests
import json
from django.shortcuts import render, redirect
from oauth.models import SuliceUser
from django.conf import settings
# Create your views here.
s = settings

def oauth_login(request):
    #url = drops_url + '/oauth2/code/get/sluice'
    url = s.DROPS_URL + s.DROPS_AUTH_CODE_PATH + s.DROPS_CLIENT_ID
    print(url)
    return redirect(url)

def oauth_redirect_url(request, code):
    token_query = {'grant_type':s.DROPS_GRAND_TYPE, 
                'client_id':s.DROPS_CLIENT_ID, 
                'code':code, 
                'redirect_uri':s.DROPS_REDIRECT_URI
                }
    request = requests.get(s.DROPS_URL + s.DROPS_TOKEN_PATH, params=token_query)
    print(request.status_code)
    token = json.loads(request.text)
    access_token = token['access_token']
    profile = requests.get(s.DROPS_URL + s.DROPS_PROFILE_PATH, params={'access_token': access_token} )
    
    
    print(access_token)
    print(request.text)
    print(profile.text)
    return redirect('http://localhost:8000/register/')
