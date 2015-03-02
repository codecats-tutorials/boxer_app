from django.conf.urls import patterns, url, include
from acl.views.main import Main


urlpatterns = patterns('',
   url(r'^', Main.as_view(), name='index'),

)