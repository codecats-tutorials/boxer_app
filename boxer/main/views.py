from django.shortcuts import render
from django.views.generic import TemplateView


class Main(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})



class View(TemplateView):
    template_name = 'views/'

    def get(self, request, *args, **kwargs):
        self.template_name += kwargs.get('template')
        return self.render_to_response({})