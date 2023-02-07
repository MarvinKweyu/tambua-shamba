from django.contrib.gis.db import models
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify

from soilcarbon.helpers.model_helpers import validate_is_csv


class SourceFile(models.Model):
    """CSV collection info from where field collection happens"""

    title = models.CharField(max_length=500)
    file_slug = models.SlugField(max_length=500, unique=True)
    csv_file = models.FileField(
        upload_to="field_sources/%Y/%m/%d/",
        validators=[FileExtensionValidator(allowed_extensions=["csv"])],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title"]

    def save(self, *args, **kwargs):
        """Use the csv_file name as the title"""
        if not self.title or not self.slug:
            self.title = slugify(self.csv_file.name)
            self.file_slug = slugify(self.csv_file.name)
        super().save(*args, **kwargs)

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
    geographical_boundaries = models.MultiPolygonField(geography=True)
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
