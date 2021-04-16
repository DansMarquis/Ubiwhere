from rest_framework import viewsets, permissions
from .models import Occurrence
from .serializers import OccurrenceSerializer
from django_filters import rest_framework as filters
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import Distance

class OccurrenceFilter(filters.FilterSet):
    author = filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Occurrence
        fields = ('author', 'category')
    
class OccurrenceView(viewsets.ModelViewSet):
    queryset=Occurrence.objects.all()
    serializer_class=OccurrenceSerializer
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
    filterset_class = OccurrenceFilter
    
class SearchResultsView(viewsets.ModelViewSet):
    serializer_class=OccurrenceSerializer
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
    filterset_class = OccurrenceFilter
    pnt = GEOSGeometry('POINT(40.646947621546595 -8.643220047471523)', srid=4326) # Ubiwhere default center Point
    queryset=Occurrence.objects.filter(location__distance_lt=(pnt, Distance(km=8))) #TODO parameter for radius
    
    


