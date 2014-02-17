#Django imports
from rest_framework import viewsets

#App imports
from f1rest.teams.serializers import TeamSerializer
from f1rest.teams.models import Team

class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Team.objects.filter(active=True).order_by('name')
    serializer_class = TeamSerializer


