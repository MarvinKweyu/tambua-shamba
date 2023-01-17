from django.db import models


class Farm(models.Model):
    """
    A single farm object in Kenya
    """

    farm_name = models.CharField(max_length=200, unique=True)
    location_boundary = models.CharField()
    soil_organic_carbon = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = "soil_organic_carbon"

    def __str__(self) -> str:
        """Human readable name for this farm object"""
        return str(self.farm_name)
