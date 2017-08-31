from django.conf.urls import url

from . import views


urlpatterns=[
    url(r'^login/$', views.oauth_login),
    url(r'^redirecturl/(?P<code>\w+)/$', views.oauth_redirect_url),
]
