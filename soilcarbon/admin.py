from django.contrib import admin
from soilcarbon.models import Farm


@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
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
