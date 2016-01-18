"""
Django settings for hvhc project.

Generated by 'django-admin startproject' using Django 1.8.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import MEDIA_ROOT, MEDIA_URL
from os.path import join

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#FILE_UPLOAD_PERMISSIONS = 0644
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!qz9m98#-ub-c(i1ppfol1y*-ia88i!ms0a!yez8)702+w29k2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
#     'django_admin_bootstrapped.bootstrap3',
	'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
# 	'permission',

	'import_export',
	
    'daotao',
    'hrm',
    'tracnghiem',
    'tuluan',
)
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # default
    'permission.backends.PermissionBackend',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'hvhc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [join(BASE_DIR,'templates'),
                 join(BASE_DIR, 'templates/tuluan/'),
                 join(BASE_DIR, 'templates/tracnghiem/'),
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

WSGI_APPLICATION = 'hvhc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'vi'

TIME_ZONE = 'Asia/Ho_Chi_Minh'

USE_I18N = True
Q = 100

USE_L10N = True

# USE_TZ = True

DATE_INPUT_FORMATS = ("%d/%m/%Y",)
DATE_FORMAT = ("%d/%m/%Y",)
TIME_FORMAT = ("%H:%M",)
TIME_INPUT_FORMATS=("%H:%M",)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
#STATIC_ROOT = '/var/www/hvhc/static/'
# STATIC_ROOT = join(BASE_DIR,'static/')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
#    '/var/www/hvhc/static/',
# 	'/var/www/hvhc/media',
# 	'/var/www/hvhc/locate',
    join(BASE_DIR, 'media'),
    join(BASE_DIR, 'locale'),
)

ADMIN_MEDIA_PREFIX='/static/admin/'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
    '/var/www/locale',
)
#MEDIA_ROOT='/var/www/hvhc/media'

DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'

MEDIA_ROOT= join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'
