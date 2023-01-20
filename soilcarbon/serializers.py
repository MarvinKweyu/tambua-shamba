from django.contrib.gis.db import models as gis_models
from rest_framework import serializers

from soilcarbon.models import Farm, SourceFile


class SourceFileSerializer(serializers.ModelSerializer):
    """ """

    farm_count = serializers.IntegerField(read_only=True)
    # file_name = serializers.IntegerField(read_only=True)

    class Meta:
        model = SourceFile
        fields = (
            "id",
            "title",
            "csv_file",
            "farm_count",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("farm_count", "title")

    def to_representation(self, instance):
        data = super().to_representation(instance)

        farm_count = Farm.objects.filter(source_file=data["id"]).count()

        data["farm_count"] = farm_count

        return data


class FarmSerializer(serializers.ModelSerializer):
    """
    JSON serializable object of the farm
    """

    class Meta:
        model = Farm
        fields = (
            "id",
            "farm_name",
            "soil_organic_carbon",
            "source_file",
            "geographical_boundaries",
            "created_at",
            "updated_at",
        )
