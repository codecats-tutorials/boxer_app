from django.http import JsonResponse
from rest_framework.views import APIView
from player.documents import Player
from player.serializers.main import PlayerSerializer

__author__ = 't'

class Main(APIView):
    def get(self, request, *args, **kwargs):
        data = Player.objects.all()
        return JsonResponse(map(lambda x: x.as_json(), data), safe=False)

    def post(self, request, *args, **kwargs):
        data = request.DATA.copy()
        player = Player(**data)
        player.save()
        return JsonResponse(data)

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass