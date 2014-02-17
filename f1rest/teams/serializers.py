#Django imports
from rest_framework import serializers

#App imports
from f1rest.teams.models import Team


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        exclude = ('active',)
