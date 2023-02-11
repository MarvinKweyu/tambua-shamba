from __future__ import absolute_import, unicode_literals

import os
from pathlib import Path

from tambuashamba.config.base import *

DEBUG = False

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

BASE_DIR = Path(__file__).resolve().parent.parent

# change this according to your domain
CORS_ALLOW_ALL_ORIGINS = True
ALLOWED_HOSTS = ["*"]
CORS_ALLOW_ALL_ORIGINS = True
