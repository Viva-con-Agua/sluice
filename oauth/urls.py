from django.conf.urls import url

from . import views


urlpatterns=[
    url(r'^login/$', views.oauth2_login),
    url(r'^redirecturl/(?P<code>\w+)/$', views.oauth2_get_token),
]
