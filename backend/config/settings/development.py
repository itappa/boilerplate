import os
from pathlib import Path

from .base import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = True
USE_TAILWIND_CDN = True

INSTALLED_APPS += ("debug_toolbar",)

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
