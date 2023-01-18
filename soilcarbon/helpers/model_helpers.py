import os
from io import BytesIO

import magic
import pandas as pd
from django.core.exceptions import ValidationError


def file_is_valid(csv_file) -> bool:
    """
    Check that the file has the relevant headers and no item is Null / empty
    returns: bool
    """

    # accepted_headers = ["Farm Name", "Geolocation Boundaries"]
    # filename = BytesIO(csv_file.read())
    # print("\n\n")
    # print("result filename", csv_file.path)

    # print("\n\n")

    # file_upload_df = pd.read_csv(csv_file.path)

    # if file_upload_df.columns not in accepted_headers:
    #     return False
    return True


def create_farms_from_file(csv_title) -> None:
    """
    Create farm objects from a CSV file upload
    returns: None
    """
    # farm = Farm.objects.get(title=csv_title)

    # file_upload_df = pd.read_csv(farm.csv_file)

    pass


def validate_is_csv(file) -> None:
    """
    Confirm that the file is a CSV file. Use mimetype as well as file extension

    Parameters
    ----------
    file
       A file object

    returns: None
    """

    valid_mime_types = ["text/csv"]
    file_mime_type = magic.from_buffer(file.read(1024), mime=True)
    if file_mime_type not in valid_mime_types:
        raise ValidationError("Unsupported file type.")
    # does it end with a .csv?
    valid_file_extensions = [".csv"]
    ext = os.path.splitext(file.name)[1]
    if ext.lower() not in valid_file_extensions:
        raise ValidationError("Unacceptable file extension.")
