from time import sleep
from django.http import JsonResponse
from rest_framework.views import APIView
from coach.documents import Coach
from coach.serializers.main import CoachSerializer

__author__ = 't'

class Main(APIView):
    def get(self, request, *args, **kwargs):
        if request.GET.get('count'):
            response = {'count': Coach.objects().count()}
        elif kwargs.get('id', False):
            coach = Coach.objects().get(pk=kwargs.get('id'))
            response = CoachSerializer(coach).data
        else:
            page = int(request.GET.get('page', 1))
            coaches = Coach.objects()[(page-1) * 5: page * 5]
            response = {'data': map(lambda x: CoachSerializer(x).data, coaches)}

        return JsonResponse(response)


    def post(self, request, *args, **kwargs):
        data = request.DATA.copy()
        serializer = CoachSerializer(data=data)
        if serializer.is_valid():
            coach = serializer.save()
            coach.save()
            response = CoachSerializer(coach).data
        else:
            data['errors'] = serializer.errors
            response = data

        return JsonResponse(response)

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass