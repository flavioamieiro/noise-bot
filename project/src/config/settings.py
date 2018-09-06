from unipath import Path

import dj_database_url
from decouple import config

BASE_DIR = Path(__file__).ancestor(3)
SRC_DIR = BASE_DIR.child('src')


TESTING = False
DEBUG = config('DEBUG', cast=bool)
SECRET_KEY = config('SECRET_KEY')
PRODUCTION = config('PRODUCTION', default=False)

ALLOWED_HOSTS = [config('APP_HOST', default='')]

INSTALLED_APPS = [
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'raven.contrib.django.raven_compat',
    'django_extensions',
    'scheduler',
    'django_rq',
    'src.core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.child('templates')],
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

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child("static")]
STATICFILES_STORAGE = config('STATICFILES_STORAGE', default='whitenoise.django.GzipManifestStaticFilesStorage')


DATABASES = {
    'default': dj_database_url.parse(config('DATABASE_URL'))
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


LANGUAGE_CODE = 'pt-BR'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Django RQ
REDIS_URL = config('REDIS_URL', default='redis://localhost:50102')
REPLY_QUEUE = 'replies'
RQ_QUEUES = {
    REPLY_QUEUE: {
        'URL': REDIS_URL,
        'DB': 0,
        'DEFAULT_TIMEOUT': 5000,
    },
}


# Admin config
SUIT_CONFIG = {
    'ADMIN_NAME': 'Noise Bot Admin',
}

import django_heroku
django_heroku.settings(locals())
