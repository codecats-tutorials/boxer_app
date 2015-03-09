from mongoengine.django.auth import User

__author__ = 't'


class UserProfile(User):
    backend = 'mongoengine.django.auth.MongoEngineBackend'
