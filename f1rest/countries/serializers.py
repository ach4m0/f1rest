#Django imports
from rest_framework import serializers

#App imports
from .models import Country


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country

