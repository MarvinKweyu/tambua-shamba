import pandas as pd
import magic
from django.contrib.gis import geos
from django.contrib.gis.geos import GEOSGeometry, fromstr
from django.db.utils import IntegrityError
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
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
        Override the viewset create method to check validity of the file and update the Farm object where necessary
        Add farms or create farm objects that have not been added from previous file uploads.
        """

        accepted_headers = [
            "Farm Name",
            "Geolocation Boundaries",
            "SOC (tonnes/hectare)",
        ]

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.is_valid():
            # before you save this file, check that the fields are valid
            pre_saved_file = serializer.validated_data["csv_file"]

            df = pd.read_csv(pre_saved_file)
            # ensure there is content in this file
            if df.empty:
                return JsonResponse(
                    {"error": "This file is empty."},
                    status=400,
                )

            print(f"{df.head()} are the columns \n")
            print(f"{accepted_headers} are accepted\n\n")
            all_columns_present = any(
                [item in accepted_headers for item in df.columns.tolist()]
            )
            if not all_columns_present:
                return JsonResponse(
                    {"error": "This file does not have the required column headers."},
                    status=400,
                )

            if df.isnull().sum().sum() > 0:
                return JsonResponse(
                    {"error": "The file has empty/ null values in its rows"},
                    status=400,
                )
            # take all rows of `Geolocation Boundaries` and confirm they are valid
            boundaries = df["Geolocation Boundaries"]
            for boundary in boundaries:
                try:
                    GEOSGeometry(boundary)
                except ValueError:
                    return JsonResponse(
                        {
                            "error": "Invalid file format. Some rows on this file have cannot be read as WKT EWKT, or HEXEWKB."
                        },
                        status=400,
                    )

        #  save this instance before creationg the Farm
        instance = serializer.save()

        # filter through this df to remove rows that do not meet the condition for valid geographical boundaries
        for index, row in df.iterrows():
            boundary = row["Geolocation Boundaries"]

            try:
                boundary = fromstr(boundary)
            except TypeError:
                return JsonResponse(
                    {
                        "error": "Invalid Gelocation boundary.Check the geolocation boundaries for all your rows and try again"
                    }
                )

            # check if we have polygons and convert to multipolygons
            if isinstance(boundary, geos.Polygon):
                boundary = geos.MultiPolygon(boundary)
            farm = Farm(
                farm_name=row["Farm Name"],
                geographical_boundaries=boundary,
                soil_organic_carbon=row["SOC (tonnes/hectare)"],
                source_file=instance,
            )

            try:
                farm.save()
            except IntegrityError:
                # go to the next row in the csv since this farm already exists
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

    @action(detail=False, methods=["get"], url_path="topfarms/(?P<count>\d+)")
    def topfarms(self, request, *args, **kwargs):
        """
        Return a list of farms with most soil organic carbon
        """
        number_of_farms = int(kwargs.get("count"))
        farms = Farm.objects.all().order_by("-soil_organic_carbon")[:number_of_farms]

        page = self.paginate_queryset(farms)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        farm_data = FarmSerializer(data=farms, many=True)
        farm_data.is_valid()
        return Response(farm_data.data)

    @action(detail=False, methods=["get"], url_path="worstfarms/(?P<count>\d+)")
    def worstfarms(self, request, *args, **kwargs):
        """
        Return a list of farms with the least soil organic carbon
        """
        number_of_farms = int(kwargs.get("count"))
        farms = Farm.objects.all().order_by("soil_organic_carbon")[:number_of_farms]

        page = self.paginate_queryset(farms)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        farm_data = FarmSerializer(data=farms, many=True)
        farm_data.is_valid()
        return Response(farm_data.data)
