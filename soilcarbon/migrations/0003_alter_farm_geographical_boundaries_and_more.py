# Generated by Django 4.1.5 on 2023-01-19 09:43

import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("soilcarbon", "0002_rename_location_boundary_farm_geographical_boundaries"),
    ]

    operations = [
        migrations.AlterField(
            model_name="farm",
            name="geographical_boundaries",
            field=django.contrib.gis.db.models.fields.PolygonField(srid=4326),
        ),
        migrations.AlterField(
            model_name="sourcefile",
            name="csv_file",
            field=models.FileField(
                upload_to="field_sources/%Y/%m/%d/",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["csv"]
                    )
                ],
            ),
        ),
    ]
