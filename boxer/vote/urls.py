from django.conf.urls import patterns, url, include
from vote.views.coach.main import Main


urlpatterns = patterns('',
    url(r'^coach/(?P<id>.+)/?', Main.as_view(), name='coach_index_one'),
)