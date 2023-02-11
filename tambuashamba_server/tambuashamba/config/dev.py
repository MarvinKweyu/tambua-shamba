from __future__ import absolute_import, unicode_literals

import os
from pathlib import Path

from tambuashamba.config.base import *

DEBUG = True

SECRET_KEY = os.getenv("SECRET_KEY")

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": os.environ.get("DATABASE_NAME"),
        "USER": os.environ.get("DATABASE_USER"),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD"),
        "HOST": os.environ.get("DATABASE_HOST"),
        "PORT": os.environ.get("DATABASE_PORT"),
    }
}

#  allow every access in local development
CORS_ALLOW_ALL_ORIGINS = True

BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = ["*"]

# display mail on console
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
