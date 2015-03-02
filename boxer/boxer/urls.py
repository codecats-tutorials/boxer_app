from django.conf.urls import patterns, include, url
from django.contrib import admin
import main

urlpatterns = patterns('',
    url(r'^', include('main.urls'), name='main'),
    url(r'^players/', include('player.urls'), name='player'),

    #remove after develop front app finished
    url(r'^(?P<resource>.+((\.js)|(\.css)|(\.css\.map)|(\.ttf)|(\.woff)|(\.woff2)))$', include('front_serve.urls'), name='front_serve'),
    url(r'^(?P<resource>.+((\.png)|(\.gif)))$', include('front_serve.urls'), name='front_serve_img'),
    url(r'^admin/', include(admin.site.urls)),
)
