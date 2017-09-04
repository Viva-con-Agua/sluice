import requests
import json
from django.db import OperationalError
from django.shortcuts import render, redirect
from oauth.models import SluiceUser
from django.conf import settings
# Create your views here.
s = settings

'''
oauth2_login redirect
'''

def oauth2_login(request):
    print(request.session)
    url = s.DROPS_URL + s.DROPS_AUTH_CODE_PATH + s.DROPS_CLIENT_ID
    print(url)
    return redirect(url)

def oauth2_get_token(request, code):
    token_query = {'grant_type':s.DROPS_GRAND_TYPE, 
                'client_id':s.DROPS_CLIENT_ID, 
                'code':code, 
                'redirect_uri':s.DROPS_REDIRECT_URI
                }
    token_request = requests.get(s.DROPS_URL + s.DROPS_TOKEN_PATH, params=token_query)
    print(token_request.status_code)
    if token_request.status_code == 200 :
        token = json.loads(token_request.text)
        access_token = token['access_token']
    else:
        raise BadRequest('no User')
    profile = requests.get(s.DROPS_URL + s.DROPS_PROFILE_PATH, params={'access_token': access_token})
    
    if profile.status_code == 200 :
        drops_user = json.loads(profile.text)
        print(drops_user)
        pool_id = drops_user['id']
        try:
            user = SluiceUser.objects.get(pk=pool_id)
        except SluiceUser.DoesNotExist:
            user = SluiceUser.objects.create_user(pool_id)
            print('\n New')
        user.is_active = True
        user.token = token
        user.save()
        request.session['pool_id'] = user.pool_id
        
    
    return redirect('http://localhost:8000/register/')
