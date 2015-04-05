from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from player.documents import Player
from player.serializers.main import PlayerSerializer


class Main(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            data = map(lambda p: {
                'description': 'bbb bb'*10,
                'player': PlayerSerializer.to_representation_raw(p)
            }, Player.champions())
            return JsonResponse(data, safe=False)
        return self.render_to_response({})



class View(TemplateView):
    template_name = 'views/'

    def get(self, request, *args, **kwargs):
        self.template_name += kwargs.get('template')
        return self.render_to_response({})