__author__ = 't'

class OrganizationsManager(object):

    @staticmethod
    def get_all(player_cls):
        return player_cls._get_collection().aggregate([
            {'$unwind': '$champion'},
            {'$group': {
                '_id': '$champion'
            }}
        ])