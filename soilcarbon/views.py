import pandas as pd
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from soilcarbon.models import Farm, SourceFile
from soilcarbon.serializers import FarmSerializer, SourceFileSerializer


class SourceFileViewSet(viewsets.ModelViewSet):
    """ """

    queryset = SourceFile.objects.all()
    serializer_class = SourceFileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["title"]

    # def create(self, request, *args, **kwargs):
    #     """
    #     Add farms or create farm objects that have not been added from previous file uploads.
    #     """
    #     # print(f"{request.data}")
    #     pre_saved_file = request.data["csv_file"]

    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)

    #     instance = serializer.save()

    #     # # path of saved file
    #     # file_path = instance.csv_file.path
    #     # print(f"Reading the file here: {file_path}")

    #     # csv_file = pd.read_csv(file_path)
    #     # for index, row in csv_file.iterrows():
    #     #     farm = Farm(
    #     #         farm_name=row["Farm Name"],
    #     #         geographical_boundaries=row["Geographical Boundaries"],
    #     #         soil_organic_carbon=row["SOC(tonnes/hectare)"],
    #     #         source_file=instance,
    #     #     )

    #     #     try:
    #     #         farm.save()
    #     #     except:
    #     #         # go to the next row  in the csv since this farm already exists
    #     #         continue

    #     return Response(serializer.data)


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
