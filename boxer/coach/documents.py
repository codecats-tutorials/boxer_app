import mongoengine
from player.documents import Player

__author__ = 't'


class Coach(mongoengine.Document):
    name = mongoengine.StringField()
    surname = mongoengine.StringField()
    #rate = mongoengine.IntField(required=False)
    rate = mongoengine.ReferenceField('vote.documents.UserCoachVote')
    players = mongoengine.ListField(mongoengine.ReferenceField(Player))

#Coach.register_delete_rule(vote.documents.UserCoachVote, 'rate', mongoengine.CASCADE)