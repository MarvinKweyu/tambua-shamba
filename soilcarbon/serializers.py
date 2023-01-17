from rest_framework import serializers
from soilcarbon.models import Farm


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
            "location_boundary",
            "created_at",
        )
