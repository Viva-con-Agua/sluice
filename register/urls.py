from django.conf.urls import include, url

from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^register/$', views.add_microservice, name='add_microservice'),
    url(r'^$', views.list_microservice, name='list_microservice')
]


