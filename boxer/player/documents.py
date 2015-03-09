import mongoengine

__author__ = 't'


class Player(mongoengine.Document):
    name = mongoengine.StringField(max_length=255, required=True)
    surname = mongoengine.StringField(max_length=255, required=True)
    avatar = mongoengine.StringField(required=False)
    champion = mongoengine.ListField(mongoengine.StringField(max_length=30), required=False)
    reach = mongoengine.IntField(max_value=300, min_value=100, required=False)
    height = mongoengine.IntField(max_value=300, min_value=100, required=False)
    description = mongoengine.StringField(required=False)

    def save(self, force_insert=False, validate=True, clean=True,
             write_concern=None,  cascade=None, cascade_kwargs=None,
             _refs=None, **kwargs):

        if self.champion is not None and isinstance(self.champion, set):
            self.champion = list(self.champion)

        super(Player, self).save(
            force_insert, validate, clean, write_concern, cascade, cascade_kwargs, _refs, **kwargs
        )
