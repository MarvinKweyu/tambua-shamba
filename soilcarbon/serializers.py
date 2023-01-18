from rest_framework import serializers

from soilcarbon.models import Farm, SourceFile


class SourceFileSerializer(serializers.ModelSerializer):
    """ """

    class Meta:
        model = SourceFile
        fields = ("id", "csv_file", "created_at", "updated_at")


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
            "geographical_boundaries",
            "created_at",
            "updated_at",
        )
