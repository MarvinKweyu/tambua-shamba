import django_filters.rest_framework
import pandas as pd
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

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

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        file_path = instance.csv_file.path

        # print(file_path)

        csv_file = pd.read_csv(file_path)

        print("\nFile detail: ", csv_file.head())

        return Response(serializer.data)


class FarmViewSet(viewsets.ModelViewSet):
    """
    Soil carbon listing and detail views
    """

    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["farm_name"]
