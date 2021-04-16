from os import name
from rest_framework import routers
from .views import OccurrenceView, SearchResultsView

router=routers.DefaultRouter()
router.register('occurrences', OccurrenceView)
router.register('searchRadius', SearchResultsView)