import mongoengine

__author__ = 't'


class Player(mongoengine.Document):
    name = mongoengine.StringField(max_length=255)
    surname = mongoengine.StringField(max_length=255)
    #
    # 'id': 1,
    #       'name': 'Wladimir',
    #       'surname': 'Klitschko',
    #       'champion': ['IBF', 'WBA'],
    #       'avatar': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTd0CPzV7QBK5hhN2WT9YTdeqmnml6UT5OSDKC3YGqqXI5cnWqK'
    #     }], safe=False)
