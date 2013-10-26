import datetime
from haystack import indexes
from .models import *


class PageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True,  model_attr="text")
    origin = indexes.CharField(model_attr="filename")

    def get_model(self):
        return Issue

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
