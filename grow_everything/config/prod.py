from __future__ import absolute_import, unicode_literals

import os
from pathlib import Path

from grow_everything.config.base import *

DEBUG = False

SECRET_KEY = os.getenv(
    "SECRET_KEY", "a^(6eqi@if&6lyt0h1od^o450!8h8@s0*x_rf9(bx(3fiuhj*6"
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
