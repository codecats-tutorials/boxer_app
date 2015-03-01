
from django.conf.urls import patterns, url, include
from main import views
from django.contrib.auth.views import logout

urlpatterns = patterns('',
   url(r'^$', views.Main.as_view(), name='index'),
   url(r'^views/(?P<template>.+)$', views.View.as_view(), name='view'),
)
