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


def get_all_champions(player_cls, skip=0, limit=10, project=None):
    query = [
        {'$unwind': '$champion'},
        {'$match': {'champion': {'$exists': True}}},
        {'$skip': skip},
        {'$limit': limit}
    ]
    if project is not None:
        query.append(dict(map(lambda x: (x, True), project)))
    return player_cls._get_collection().aggregate(query)
