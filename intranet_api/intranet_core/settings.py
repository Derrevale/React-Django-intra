"""
Django settings for intranet_core project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import logging
import os
from pathlib import Path

import ldap
from django.conf import settings
from django_auth_ldap.config import LDAPSearch, ActiveDirectoryGroupType

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-oe)99z658^lmt)nh(m-y9z*w@m2v9@t!kxuyn(p+4r_g0h7(!^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # SILVA Medical
    'blog',
    'galerie',
    'documents',
    'calendrier',
    'import_ad',

    # 3rd party
    'colorfield',
    'ckeditor',

    'rest_framework',
    'drf_yasg',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

ROOT_URLCONF = 'intranet_core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'intranet_core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'Europe/london'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Logging
logger = logging.getLogger('intranet_api')
logger.addHandler(logging.StreamHandler())

# Set the default level
if settings.DEBUG:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

# LDAP Authentication
AUTH_LDAP_SERVER_URI = 'ldap://10.1.0.80:389'
AUTH_LDAP_BIND_DN = 'cn=Administrator,cn=Users,dc=SILVA,dc=LAN'
AUTH_LDAP_BIND_PASSWORD = 'anointer-parade-aptly-refutable'

AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=SILVA,dc=silva,dc=lan",
                                   ldap.SCOPE_SUBTREE,
                                   "sAMAccountName=%(user)s")

AUTH_LDAP_USER_ATTR_MAP = {
    'username': 'sAMAccountName',
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail"
}

AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    "dc=SILVA,dc=LAN",
    ldap.SCOPE_SUBTREE,
    "(objectCategory=Group)",
)
AUTH_LDAP_GROUP_TYPE = ActiveDirectoryGroupType(name_attr="cn")

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": 'CN=Administrateurs IT,OU=SILVA,DC=silva,DC=lan',
    "is_staff": 'CN=Administrateurs IT,OU=SILVA,DC=silva,DC=lan',
    "is_superuser": 'CN=Administrateurs IT,OU=SILVA,DC=silva,DC=lan',
}

AUTH_LDAP_FIND_GROUP_PERMS = True
AUTH_LDAP_CACHE_GROUPS = True

AUTHENTICATION_BACKENDS = (
    "django_auth_ldap.backend.LDAPBackend",
    "django.contrib.auth.backends.ModelBackend",
)

AUTH_LDAP_CONNECTION_OPTIONS = {
    ldap.OPT_X_TLS_REQUIRE_CERT: False,
    ldap.OPT_REFERRALS: 0
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

# OCR Search configuration
SILVA_SEARCH_PROCESS_URL = "http://localhost:8001/process"
SILVA_SEARCH_URL = "http://localhost:8001/search"
