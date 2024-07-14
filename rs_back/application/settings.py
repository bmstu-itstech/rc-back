import sys
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent

PYTEST = "pytest" in sys.argv[0]
env_path = BASE_DIR / "local/test.env" if PYTEST else BASE_DIR / ".env"

env = environ.Env()
environ.Env.read_env(env.str("ENV_PATH", str(env_path)))

VERSION = env.str("VERSION", default="0.1.0")
SECRET_KEY = env.str("SECRET_KEY", default="my-secret-key")
DEBUG = env.bool("DEBUG", default=False)
if PYTEST:
    DEBUG = False

ALLOWED_HOSTS = env.str("ALLOWED_HOSTS", default="*").split(",")
CSRF_TRUSTED_ORIGINS = env.str(
    "CSRF_TRUSTED_ORIGINS", default="https://darleet.com"
).split(",")

CORS_ORIGIN_ALLOW_ALL = env.bool("CORS_ORIGIN_ALLOW_ALL", default=False)
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
    'django_cleanup.apps.CleanupConfig',
    'sorl.thumbnail',
    'debug_toolbar',
    'rest_framework',
    'drf_yasg',
    'corsheaders',
]

PROJECT_APPS = [
    "rs_back.achievement",
    "rs_back.core",
    "rs_back.director",
    "rs_back.events",
    "rs_back.hardathon",
    "rs_back.news",
    "rs_back.partners",
    "rs_back.static_data",
]

INSTALLED_APPS += PROJECT_APPS

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

ROOT_URLCONF = 'rs_back.application.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'rs_back/core/templates'
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

WSGI_APPLICATION = 'rs_back.application.wsgi.application'

DATABASES = {
    "tests": {
        "ENGINE": "django.db.backends.sqlite3",
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    "main": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env.str("POSTGRES_DB", default="postgres"),
        "USER": env.str("POSTGRES_USER", default="postgres"),
        "PASSWORD": env.str("POSTGRES_PASSWORD", default="postgres"),
        "HOST": env.str("POSTGRES_HOST", default="127.0.0.1"),
        "PORT": env.str("POSTGRES_PORT", default="5432"),
    },
}

default_db = "tests" if PYTEST else "main"
DATABASES["default"] = DATABASES.get(default_db)

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

STATIC_URL = "/django_static/"
MEDIA_URL = "/django_media/"
STATIC_ROOT = BASE_DIR / "django_static"
MEDIA_ROOT = BASE_DIR / "django_media"

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
