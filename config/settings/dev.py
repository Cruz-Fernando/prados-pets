"""
Settings de desarrollo — SQLite, DEBUG activo.
Uso local del equipo mientras trabajamos en E1.
"""

from .base import *  # noqa: F401,F403
from .base import BASE_DIR

SECRET_KEY = "django-insecure-dev-key-cambiar-en-produccion"

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
