import mongoengine
from boxer.settings import MONGOENGINE_USER_DOCUMENT
from coach.documents import Coach

__author__ = 't'


class UserCoachVote(mongoengine.Document):
    user = mongoengine.ReferenceField(MONGOENGINE_USER_DOCUMENT)
    coach = mongoengine.ReferenceField(Coach)
    rate = mongoengine.IntField(required=False)
