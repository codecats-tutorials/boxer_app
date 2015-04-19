from django.http import JsonResponse
from mongoengine import DoesNotExist
from rest_framework.views import APIView
from coach.documents import Coach
from vote.documents import UserCoachVote

__author__ = 't'


class Main(APIView):
    def post(self, request, *args, **kwargs):
        try:
            vote = UserCoachVote.objects.get(user=request.user, coach=kwargs.get('id'))
        except DoesNotExist:
            vote = UserCoachVote(user=request.user, coach=kwargs.get('id'))
        vote.rate =  request.DATA.get('rate')
        vote.save()
        return JsonResponse({})