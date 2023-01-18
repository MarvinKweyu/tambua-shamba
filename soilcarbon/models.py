from django.db import models
from django.utils.text import slugify
from soilcarbon.helpers.model_helpers import (
    file_is_valid,
    validate_is_csv,
    create_farms_from_file,
)


class SourceFile(models.Model):
    """CSV collection info from where field collection happens"""

    title = models.CharField(max_length=500)
    csv_file = models.FileField(
        upload_to="field_sources/%Y/%m/%d/", validators=(validate_is_csv,)
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title"]

    def save(self, *args, **kwargs):
        """Use the csv_file name as the title"""
        if file_is_valid(self.csv_file):
            if not self.title:
                self.title = slugify(self.title)
                super().save(*args, **kwargs)
                # add farms or create farm objects that have not been added from previous file uploads
                # ? background task
                # create_farms_from_file(self.title)

    def __str__(self):
        return self.title


class Farm(models.Model):
    """
    A single farm object in Kenya
    """

    farm_name = models.CharField(max_length=200, unique=True)
    source_file = models.ForeignKey(
        SourceFile, related_name="farms", on_delete=models.CASCADE
    )
    location_boundary = models.CharField(max_length=500)
    soil_organic_carbon = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("soil_organic_carbon",)
        # verbose_name = "farm"
        # verbose_name_plural = "farms"

    def __str__(self) -> str:
        """Human readable name for this farm object"""
        return str(self.farm_name)
