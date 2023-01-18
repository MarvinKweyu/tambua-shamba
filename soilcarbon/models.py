import pandas as pd
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from soilcarbon.helpers.model_helpers import validate_is_csv


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
        if not self.title:
            self.title = slugify(self.title)
            super().save(*args, **kwargs)

    def __str__(self):
        return self.title


@receiver(pre_save, sender=SourceFile)
def check_file_validity(sender, instance, **kwargs):
    """
    Check if the file has the correct column headers and whether it has content with no null values
    """
    csv_file = instance.csv_file

    # Check the file's validity here
    df = pd.read_csv(csv_file)
    # ensure there is content in this file
    if df.empty:
        raise ValidationError("This file is empty.")

    pre_save.connect(check_file_validity, sender=SourceFile)


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
