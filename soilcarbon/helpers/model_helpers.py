import os

import magic
from django.core.exceptions import ValidationError


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
