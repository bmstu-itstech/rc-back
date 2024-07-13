import os
import sys
from pathlib import Path

from dotenv import load_dotenv

import environ

BASE_DIR = Path(__file__).resolve().parent.parent

PYTEST = "pytest" in sys.argv[0]
env_path = BASE_DIR / "local/test.env" if PYTEST else BASE_DIR / ".env"

env = environ.Env()
environ.Env.read_env(env.str("ENV_PATH", str(env_path)))

VERSION = env.str("VERSION", default="0.1.0")
SECRET_KEY = env.str("SECRET_KEY", default="my-secret-key")
LOCAL_MEDIA = env.bool("LOCAL_MEDIA", default=True)
DEBUG = env.bool("DEBUG", default=False)
if PYTEST:
    DEBUG = False

ALLOWED_HOSTS = env.str("ALLOWED_HOSTS", default="*").split(",")
CSRF_TRUSTED_ORIGINS = env.str(
    "CSRF_TRUSTED_ORIGINS", default="https://darleet.com"
).split(",")

CORS_ORIGIN_ALLOW_ALL = env.bool("CORS_ORIGIN_ALLOW_ALL", default=True)
CORS_ALLOWED_ORIGINS = env.str(
    "CORS_ALLOWED_ORIGINS", default="https://darleet.com"
).split(",")

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'events.apps.EventsConfig',
    'partners.apps.PartnersConfig',
    'hardathon.apps.HardathonConfig',
    'django_cleanup.apps.CleanupConfig',
    'sorl.thumbnail',
    'debug_toolbar',
    'achievement.apps.AchievementConfig',
    'news.apps.NewsConfig',
    'director.apps.DirectorConfig',
    'static_data.apps.StaticDataConfig',
    'rest_framework',
    'drf_yasg',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'robotechnics.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'core/templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'robotechnics.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


STATIC_URL = "/dj_static/"
STATIC_ROOT = BASE_DIR / "static"
if LOCAL_MEDIA:
    MEDIA_URL = "/dj_media/"
    MEDIA_ROOT = BASE_DIR / "dj_media"
    STATIC_ROOT = BASE_DIR / "dj_static"

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

DATA_UPLOAD_MAX_MEMORY_SIZE = env.int(
    "DATA_UPLOAD_MAX_MEMORY_SIZE", default=1024 * 1024 * 5  # 5 MB
)
FILE_UPLOAD_MAX_MEMORY_SIZE = env.int(
    "FILE_UPLOAD_MAX_MEMORY_SIZE", default=1024 * 1024 * 500  # 500 MB
)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_EXPOSE_HEADERS = ['Content-Type', 'X-CSRFToken']
CORS_ALLOW_CREDENTIALS = True
