from __future__ import absolute_import, unicode_literals

import os
from pathlib import Path

from grow_everything.config.base import *

DEBUG = False

SECRET_KEY = os.getenv(
    "SECRET_KEY", "django-insecure-pz800nay^^4r7=kjtyca-7&ddgp%9x)f1rj1o1%7-g-(hug%30"
)

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": os.environ.get("DATABASE_NAME", "soilcarbon"),
        "USER": os.environ.get("DATABASE_USER", "soilcarbon"),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD", "soilcarbon"),
        "HOST": os.environ.get("DATABASE_HOST", "db"),
        "PORT": os.environ.get("DATABASE_PORT", "5432"),
    }
}

BASE_DIR = Path(__file__).resolve().parent.parent

# change this according to your domain
CORS_ALLOW_ALL_ORIGINS = True
ALLOWED_HOSTS = ["*"]
CORS_ALLOW_ALL_ORIGINS = True
