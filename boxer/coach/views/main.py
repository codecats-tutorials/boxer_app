from django.http import JsonResponse
from rest_framework.views import APIView
from player.documents import Player
from player.serializers.main import PlayerSerializer

__author__ = 't'

class Main(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse({})

    def post(self, request, *args, **kwargs):
        pass

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass