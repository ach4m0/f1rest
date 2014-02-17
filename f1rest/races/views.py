#Django imports
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

#App imports
from .serializers import RaceSerializer, SeasonSerializer, GrandPrixSerializer
from .models import Race, Season, GrandPrix, Results

class RaceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Race.objects.filter(active=True).order_by('id')
    serializer_class = RaceSerializer

class SeasonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Season.objects.filter(active=True).order_by('year')
    serializer_class = SeasonSerializer

class GrandPrixViewSet(viewsets.ReadOnlyModelViewSet):
    season = Season.objects.get(active=True)
    queryset = GrandPrix.objects.filter(season=season).order_by('practice1_datetime')
    serializer_class = GrandPrixSerializer

