from django.conf.urls import patterns, url, include
from player import views
from player.views.main import Main


urlpatterns = patterns('',
   url(r'^(?P<id>\d+)/', Main.as_view(), name='index_one'),
   url(r'^', Main.as_view(), name='index'),

)