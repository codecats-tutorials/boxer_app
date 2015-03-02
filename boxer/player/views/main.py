from django.http import JsonResponse
from rest_framework.views import APIView

__author__ = 't'

class Main(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse([{
          'id': 1,
          'name': 'Wladimir',
          'surname': 'Klitschko',
          'champion': ['IBF', 'WBA'],
          'avatar': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTd0CPzV7QBK5hhN2WT9YTdeqmnml6UT5OSDKC3YGqqXI5cnWqK'
        }], safe=False)
