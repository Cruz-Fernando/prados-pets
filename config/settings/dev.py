"""
Settings de desarrollo — SQLite por defecto; si el entorno tiene las
variables DB_* (ver .env.example) usa la base PostgreSQL compartida
del equipo en su lugar.
Uso local del equipo mientras trabajamos en E1.
"""

import os

from .base import *  # noqa: F401,F403
from .base import BASE_DIR

SECRET_KEY = "django-insecure-dev-key-cambiar-en-produccion"

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Si hay variables DB_* en el entorno (cargadas desde .env), usamos la
# PostgreSQL compartida del equipo. Si no están, cada quien sigue
# trabajando con su propio db.sqlite3 local sin configurar nada más.
if os.environ.get("DB_HOST"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("DB_NAME", "postgres"),
            "USER": os.environ["DB_USER"],
            "PASSWORD": os.environ["DB_PASSWORD"],
            "HOST": os.environ["DB_HOST"],
            "PORT": os.environ.get("DB_PORT", "5432"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
