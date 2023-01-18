import pandas as pd
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.http import JsonResponse
from django.utils.text import slugify

from soilcarbon.helpers.model_helpers import validate_is_csv


class SourceFile(models.Model):
    """CSV collection info from where field collection happens"""

    title = models.CharField(max_length=500)
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
        if not self.title:
            self.title = slugify(self.csv_file.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


@receiver(pre_save, sender=SourceFile)
def check_file_validity(sender, instance, **kwargs):
    """
    Check if the file has the correct column headers and whether it has content with no null values
    """
    # Todo: return an error to the API instead of throwing the error page
    accepted_headers = ["Farm Name", "Geolocation Boundaries", "SOC (tonnes/hectare)"]
    csv_file = instance.csv_file

    # Check the file's validity here
    df = pd.read_csv(csv_file)
    # ensure there is content in this file
    if df.empty:
        raise ValidationError("This file is empty.")

    all_columns_present = any(
        [item in accepted_headers for item in df.columns.tolist()]
    )
    if not all_columns_present:
        ValidationError("The file has empty/ null values in its rows")
        return JsonResponse(
            {"error": "This file does not have the required column headers."},
            status=400,
        )

    if df.isnull().sum().sum() > 0:
        ValidationError("The file has empty/ null values in its rows")
        return JsonResponse(
            {"error": "The file has empty/ null values in its rows"},
            status=400,
        )

    pre_save.connect(check_file_validity, sender=SourceFile)


@receiver(post_save, sender=SourceFile)
def create_farms(sender, instance, **kwargs):
    """Add farms or create farm objects that have not been added from previous file uploads."""
    csv_file = instance.csv_file
    # Check the file's validity here
    df = pd.read_csv(csv_file)

    for index, row in df.iterrows():
        farm = Farm(
            farm_name=row["Farm Name"],
            geographical_boundaries=row["Geolocation Boundaries"],
            soil_organic_carbon=row["SOC (tonnes/hectare)"],
            source_file=instance,
        )

        try:
            farm.save()
        except:
            # go to the next row  in the csv since this farm already exists
            continue

    post_save.connect(create_farms, sender=SourceFile)


class Farm(models.Model):
    """
    A single farm object in Kenya
    """

    farm_name = models.CharField(max_length=200, unique=True)
    source_file = models.ForeignKey(
        SourceFile, related_name="farms", on_delete=models.CASCADE
    )
    geographical_boundaries = models.CharField(max_length=500)
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
