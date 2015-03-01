from mimetypes import read_mime_types
import mimetypes
import urllib
from django.http import Http404, HttpResponse
from django.views.generic import TemplateView
import os
from os.path import exists
from boxer.settings import STATICFILES_DIRS


class Main(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        resourse = kwargs.get('resource')
        for path in STATICFILES_DIRS:
            file = '{}/{}'.format(path, resourse)
            if exists(file):
                with open(file, 'rb') as f:
                    url = urllib.pathname2url(file)
                    return HttpResponse(f, content_type=mimetypes.guess_type(url)[0])
        raise Http404(u'Not found {}'.format(resourse))