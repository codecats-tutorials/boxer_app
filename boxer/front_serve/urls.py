from django.conf.urls import patterns, url, include
from front_serve import views


urlpatterns = patterns('',
   url(r'^', views.Main.as_view(), name='index'),
)