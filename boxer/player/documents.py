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
    #
    # 'id': 1,
    #       'name': 'Wladimir',
    #       'surname': 'Klitschko',
    #       'champion': ['IBF', 'WBA'],
    #       'avatar': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTd0CPzV7QBK5hhN2WT9YTdeqmnml6UT5OSDKC3YGqqXI5cnWqK'
    #     }], safe=False)
