from django.conf.urls import patterns, include, url
from django.contrib import admin
import main

urlpatterns = patterns('',
    url(r'^', include('main.urls'), name='main'),
    url(r'^coaches/?', include('coach.urls'), name='coach'),
    url(r'^players/?', include('player.urls'), name='player'),
    url(r'^acl/?', include('acl.urls'), name='acl'),
    url(r'^organizations/?', include('organizations.urls'), name='organizations'),
    url(r'^users/?', include('userprofile.urls'), name='users'),
    url(r'^vote/?', include('vote.urls'), name='vote'),

    (r'^search/', include('haystack.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
