#Django imports
from rest_framework import serializers

#App imports
from .models import Race, Season, GrandPrix, Results

class RaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Race
        exclude = ('active',)

class SeasonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Season
        exclude = ('active',)

class GrandPrixSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GrandPrix

