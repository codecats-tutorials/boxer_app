from haystack import indexes
from player.documents import Player


class PlayerIndex(indexes.SearchIndex, indexes.Indexable):
    name = indexes.CharField(model_attr='name')
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Player

    def index_queryset(self, using=None):
        return self.get_model().objects()