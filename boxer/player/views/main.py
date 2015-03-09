from django.http import JsonResponse
from rest_framework.views import APIView
from player.documents import Player
from player.serializers.main import PlayerSerializer

__author__ = 't'

class Main(APIView):
    def get(self, request, *args, **kwargs):
        if kwargs.get('id', False):
            player = Player.objects(pk=kwargs.get('id')).limit(1)[0]
            return JsonResponse(PlayerSerializer(player).data)
        else:
            data = Player.objects.only('name', 'surname', 'champion', 'avatar').all().limit(20)
            return JsonResponse(map(lambda x: PlayerSerializer(x).data, data), safe=False)

    def post(self, request, *args, **kwargs):
        data = request.DATA.copy()
        serializer = PlayerSerializer(data=data)
        if serializer.is_valid():
            player = serializer.save()
            player.save()
            return JsonResponse(PlayerSerializer(player).data)
        else:
            data['errors'] = serializer.errors
            return JsonResponse(data)

    def put(self, request, *args, **kwargs):
        data = request.DATA.copy()
        if 'champion' in data and not data['champion']:
            data['champion'] = None
        player = Player.objects(pk=data.get('id')).limit(1)[0]
        serializer = PlayerSerializer(player, data=data)
        if serializer.is_valid():
            player = serializer.save()
            player.save()
            return JsonResponse(serializer.data)
        else:
            data['errors'] = serializer.errors
            return JsonResponse(data)

    def delete(self, request, *args, **kwargs):
        Player.objects(pk=kwargs.get('id')).delete()
        return JsonResponse(kwargs)