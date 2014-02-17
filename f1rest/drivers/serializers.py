#Django imports
from rest_framework import serializers

#App imports
from f1rest.drivers.models import Driver


class DriverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Driver
        exclude = ('active',)
