from rest_framework import serializers

from .models import MapEntity


class MapEntitySerializer(serializers.ModelSerializer):

    class Meta:
        model = MapEntity
        fields = ('layer', 'entity', 'data')
