from __future__ import absolute_import, unicode_literals

import os
from pathlib import Path

# from dotenv import load_dotenv

from grow_everything.config.base import *

# load_dotenv()

DEBUG = True

# SECRET_KEY = os.getenv("SECRET_KEY")
SECRET_KEY = "django-insecure-pz800nay^^4r7=kjtyca-7&ddgp%9x)f1rj1o1%7-g-(hug%30"


#  allow every access in local development
CORS_ALLOW_ALL_ORIGINS = True

BASE_DIR = Path(__file__).resolve().parent.parent
# use image db
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


ALLOWED_HOSTS = ["*"]
CORS_ALLOW_ALL_ORIGINS = True

# display mail on console
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
