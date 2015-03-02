from django.http import JsonResponse
from rest_framework.views import APIView

__author__ = 't'

class Main(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(['BOXERS'], safe=False)
