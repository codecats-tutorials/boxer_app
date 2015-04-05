import mongoengine
from player.documents import Player

__author__ = 't'


class Coach(mongoengine.Document):
    name = mongoengine.StringField()
    surname = mongoengine.StringField()
    rate = mongoengine.IntField()
    players = mongoengine.ListField(mongoengine.ReferenceField(Player))