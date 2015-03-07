import mongoengine

__author__ = 't'


class Player(mongoengine.Document):
    name = mongoengine.StringField(max_length=255, required=True)
    surname = mongoengine.StringField(max_length=255, required=True)
    #todo: check new fields
    avatar = mongoengine.StringField(required=False)
    champion = mongoengine.ListField(mongoengine.StringField(max_length=30), required=False)
    def as_json(self):
        return dict(
            id=str(self.pk), name=self.name, surname=self.surname,
            champion=self.champion, avatar=self.avatar
        )

    def save(self, force_insert=False, validate=True, clean=True,
             write_concern=None,  cascade=None, cascade_kwargs=None,
             _refs=None, **kwargs):

        if self.champion is not None and isinstance(self.champion, set):
            self.champion = list(self.champion)

        super(Player, self).save(
            force_insert, validate, clean, write_concern, cascade, cascade_kwargs, _refs, **kwargs
        )
