from pathlib import Path
import os
import logging
import environ
from datetime import timedelta
import dj_database_url
import sys
from dotenv import load_dotenv

env = environ.Env()
environ.Env.read_env()

ENVIRONMENT = env

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()


SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = True

DOMAIN = os.environ.get('DOMAIN')


ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

WEBSITE_URL = os.environ.get('WEBSITE_URL')


DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

APPS = [
    'apps.users',
    'apps.authentication',
    'apps.general',
    'apps.video',
]

THIRD_PARTY_APPS = [
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'storages',
]

INSTALLED_APPS = DJANGO_APPS + APPS + THIRD_PARTY_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = "core.urls"

SITE_ID = 1

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-width',
]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOWED_ORIGINS = [
    f"https://{WEBSITE_URL}",
    f"http://{WEBSITE_URL}",
    f"http://localhost:8000",
    f"http://127.0.0.1:8000",

]

CSRF_TRUSTED_ORIGINS = [
    f"https://{WEBSITE_URL}",
    f"http://{WEBSITE_URL}",
]

SESSION_COOKIE_DOMAIN = WEBSITE_URL

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True

SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'core.wsgi.application'


# database setup
DATABASES={
    'default':{
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME':'defaultdb',
        'USER':'doadmin',
        'PASSWORD':'AVNS_ocsk8ND3TYjrIC-KZmO',
        'HOST':'db-postgresql-fra1-39659-do-user-15829099-0.c.db.ondigitalocean.com',
        'PORT':'25060',
        'sslmode' :'require',
   }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# STATIC

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"
STATICFILES_DIR = os.path.join(BASE_DIR, "staticfiles")

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"


AWS_LOCATION_STATIC = 'static'
AWS_LOCATION_MEDIA = 'media'

STATICFILES_DIR = [
    os.path.join(BASE_DIR, "static"),
]
MEDIAFILES_DIRS = [
    os.path.join(BASE_DIR, 'media'),
]

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ENABLED = True
AWS_S3_SECURE_URLS = True


DATA_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 3000
FILE_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 3000

AWS_ACCESS_KEY_ID = 'AKIA4MTWMNE24K2W7ZEJ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'bucket-video-aws'
AWS_S3_SIGNATURE_NAME = 's3v4'
AWS_S3_REGION_NAME = 'ap-southeast-1'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_VERIFY = True
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
}
AWS_QUERYSTRING_EXPIRE = 5



# rest-faramework
REST_FRAMEWORK = {
    "EXCEPTION_HANDLER": "rest_framework.views.exception_handler",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT', ),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10080),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
    'ROTATE_REFRESFH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_TOKEN_CLASSES': (
        'rest_framework_simplejwt.tokens.AccessToken',
    )
}


# cors

CORS_ORIGIN_WHITELIST = [
    'http://127.0.0.1:8000',
    'http://localhost:5173',
    'https://walrus-app-8p5bd.ondigitalocean.app',
    'http://frontend-bice-sigma.vercel.app',
    'https://www.frontend-bice-sigma.vercel.app',
    'https://frontend-bice-sigma.vercel.app',
]


CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:8000',
    'http://localhost:5173',
    'https://walrus-app-8p5bd.ondigitalocean.app',
    'http://frontend-bice-sigma.vercel.app',
    'https://www.frontend-bice-sigma.vercel.app',
    'https://frontend-bice-sigma.vercel.app',
]

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:8000',
    'http://localhost:5173',
    'https://walrus-app-8p5bd.ondigitalocean.app',
    'http://frontend-bice-sigma.vercel.app',
    'https://www.frontend-bice-sigma.vercel.app',
    'https://frontend-bice-sigma.vercel.app',
]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = "users.User"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": False,
        },
    },
}