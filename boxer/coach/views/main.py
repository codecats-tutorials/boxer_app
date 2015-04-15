from django.http import JsonResponse
from rest_framework.views import APIView
from coach.documents import Coach
from coach.serializers.main import CoachSerializer

__author__ = 't'

class Main(APIView):
    def get(self, request, *args, **kwargs):
        page = int(request.GET.get('page', 1))
        coaches = Coach.objects()[(page-1) * 5: page * 5]
        return JsonResponse({'data': map(lambda x: CoachSerializer(x).data, coaches)})

    def post(self, request, *args, **kwargs):
        data = request.DATA.copy()
        serializer = CoachSerializer(data=data)
        if serializer.is_valid():
            coach = serializer.save()
            coach.save()
            return JsonResponse(CoachSerializer(coach).data)
        else:
            data['errors'] = serializer.errors
            return JsonResponse(data)

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass