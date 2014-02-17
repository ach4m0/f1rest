#Django imports
from rest_framework import viewsets

#App imports
from f1rest.drivers.serializers import DriverSerializer
from f1rest.drivers.models import Driver

class DriverViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Driver.objects.filter(active=True).order_by('shortname')
    serializer_class = DriverSerializer


