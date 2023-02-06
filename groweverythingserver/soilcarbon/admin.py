from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from soilcarbon.models import Farm, SourceFile


@admin.register(Farm)
class FarmAdmin(OSMGeoAdmin):
    list_display = (
        "id",
        "farm_name",
        "soil_organic_carbon",
        "created_at",
    )
    list_filter = [
        "created_at",
    ]
    search_fields = ["farm_name", "soil_organic_carbon"]


@admin.register(SourceFile)
class SourceFileAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "csv_file", "created_at")
    list_filter = [
        "created_at",
    ]
    search_fields = ["title"]
