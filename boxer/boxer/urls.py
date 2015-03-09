from django.conf.urls import patterns, include, url
from django.contrib import admin
import main

urlpatterns = patterns('',
    url(r'^', include('main.urls'), name='main'),
    url(r'^players/?', include('player.urls'), name='player'),
    url(r'^acl/?', include('acl.urls'), name='acl'),
    url(r'^organizations/?', include('organizations.urls'), name='organizations'),
    url(r'^users/?', include('userprofile.urls'), name='users'),

    url(r'^admin/', include(admin.site.urls)),
)
