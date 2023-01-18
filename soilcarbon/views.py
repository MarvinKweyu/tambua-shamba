import pandas as pd
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.response import Response

from soilcarbon.models import Farm, SourceFile
from soilcarbon.serializers import FarmSerializer, SourceFileSerializer


class SourceFileViewSet(viewsets.ModelViewSet):
    """ """

    queryset = SourceFile.objects.all()
    serializer_class = SourceFileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["title"]

    def create(self, request, *args, **kwargs):
        """
        Add farms or create farm objects that have not been added from previous file uploads.
        """
        pre_saved_file = request.data["csv_file"]
        csv_before_save = pd.read_csv(pre_saved_file)
        accepted_headers = ["Farm Name", "Geolocation Boundaries"]

        # csv has all the columns that we need to create a farm object
        all_columns_present = any(
            [item in accepted_headers for item in csv_before_save.columns.tolist()]
        )

        if not all_columns_present:
            return JsonResponse(
                {"error": "This file does not have the required column headers."},
                status=400,
            )

        # is there any null row?
        if csv_before_save.isnull().sum().sum() > 0:
            return JsonResponse(
                {"error": "The file has empty/ null values in its rows"},
                status=400,
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        # path of saved file
        file_path = instance.csv_file.path

        csv_file = pd.read_csv(file_path)
        for index, row in csv_file.iterrows():
            farm = Farm(
                farm_name=row["Farm Name"],
                geographical_boundaries=row["Geographical Boundaries"],
                soil_organic_carbon=row["SOC(tonnes/hectare)"],
                source_file=instance,
            )

            try:
                farm.save()
            except:
                # go to the next row  in the csv since this farm already exists
                continue

        return Response(serializer.data)


class FarmViewSet(viewsets.ModelViewSet):
    """
    Soil organic carbon listing and detail views
    """

    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["farm_name"]
