from django.conf.urls import patterns, url
from userprofile.views.login import LoginView
from userprofile.views.logout import LogoutView

__author__ = 't'

urlpatterns = patterns('',
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^logout$', LogoutView.as_view(), name='logout'),
)