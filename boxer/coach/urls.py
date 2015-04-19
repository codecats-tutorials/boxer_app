from django.conf.urls import patterns, url, include
from coach import views
from coach.views.main import Main


urlpatterns = patterns('',
  url(r'^(?P<id>.+)/?', Main.as_view(), name='index_one'),
   url(r'^', Main.as_view(), name='index'),

)