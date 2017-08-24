from django.conf.urls import url

from . import views

'''
    .../access_token/{microservice_name} -> micro_access_token
    .../payload/{microservice_name} -> micro_payload
'''

urlpatterns=[
    url(r'^access_token/(?P<name>\w+)/$', views.micro_access_token),
    url(r'^payload/(?P<name>\w+)/$', views.micro_payload),
]
