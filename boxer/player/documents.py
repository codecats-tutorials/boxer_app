# -*- coding: utf-8 -*-

import mongoengine
from mongoengine.queryset.manager import queryset_manager
from player.doc_managers import OrganizationsManager

__author__ = 't'


class Player(mongoengine.Document):
    DIVISIONS = (('1', u'Ciężka'), ('2', u'Półciężka'))

    name = mongoengine.StringField(max_length=255, required=True)
    surname = mongoengine.StringField(max_length=255, required=True)
    avatar = mongoengine.StringField(required=False)
    champion = mongoengine.ListField(mongoengine.StringField(max_length=30), required=False)
    reach = mongoengine.IntField(max_value=300, min_value=100, required=False)
    height = mongoengine.IntField(max_value=300, min_value=100, required=False)
    description = mongoengine.StringField(required=False)
    division = mongoengine.StringField(required=False, choices=DIVISIONS)
    stance = mongoengine.StringField(required=False)
    birthdate = mongoengine.DateTimeField(required=False)

    @classmethod
    def organizations(cls):
        return OrganizationsManager.get_all(cls)

    def save(self, force_insert=False, validate=True, clean=True,
             write_concern=None,  cascade=None, cascade_kwargs=None,
             _refs=None, **kwargs):

        if self.champion is not None and isinstance(self.champion, set):
            self.champion = list(self.champion)

        super(Player, self).save(
            force_insert, validate, clean, write_concern, cascade, cascade_kwargs, _refs, **kwargs
        )
