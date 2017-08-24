from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^payload/(?P<name>\w+)/$', views.micro_payload),
]
