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
        serializer = PlayerSerializer(data=data)
        if serializer.is_valid():
            player = serializer.save()
            player.save()
            return JsonResponse(player.as_json())
        else:
            data['errors'] = serializer.errors
            return JsonResponse(data)

    def put(self, request, *args, **kwargs):
        data = request.DATA.copy()
        player = Player.objects(pk=data.get('id')).limit(1)[0]
        serializer = PlayerSerializer(player, data=data)
        if serializer.is_valid():
            player = serializer.save()
            player.save()
            return JsonResponse(player.as_json())
        else:
            data['errors'] = serializer.errors
            return JsonResponse(data)

    def delete(self, request, *args, **kwargs):
        Player.objects(pk=kwargs.get('id')).delete()
        return JsonResponse(kwargs)