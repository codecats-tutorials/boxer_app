from django.conf.urls import patterns, url, include
from organizations.views.main import Main


urlpatterns = patterns('',
   url(r'^', Main.as_view(), name='index'),

)