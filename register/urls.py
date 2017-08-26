from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^micro_add/$', views.add_microservice, name='add_microservice'),
    url(r'micro_list/$', views.list_microservice, name='list_microservice')
]


