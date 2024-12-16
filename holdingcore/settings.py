"""
Django settings for holdingcore project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# This Config is base on the API keys we added on The .env file on our Root Directory
from dotenv import load_dotenv
import os
import environ

load_dotenv() # Load environment variables from .env file


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-cf&9lnnicnaa5d0#s*)ejd(ujy*4i_6x#6-au2q!jk%6kye#n#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.ngrok-free.app']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'holdingcore_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'holdingcore.urls'

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

WSGI_APPLICATION = 'holdingcore.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    
      'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT', '5432'),  # Default port for PostgreSQL is 5432
    }
}


AUTH_USER_MODEL = 'holdingcore_app.User'


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



STATIC_ROOT = BASE_DIR / "staticfiles"  # For production (collectstatic)

STATICFILES_DIRS = [
    BASE_DIR / "static",  #used it when you have static files outsit your static folder, then u need to create an extra static folder on your main app directory where u have the manag.py file
]


# settings.py
# FLUTTERWAVE_API_KEY = 'your_test_secret_key_here'  # Use your Test Secret Key
# FLUTTERWAVE_PUBLIC_KEY = 'your_test_public_key_here'  # Use your Test Public Key
# In settings.py




FLUTTERWAVE_PUBLIC_KEY = os.getenv('FLUTTERWAVE_PUBLIC_KEY')
FLUTTERWAVE_SECRET_KEY = os.getenv('FLUTTERWAVE_SECRET_KEY')
FLUTTERWAVE_ENCRYPTION_KEY = os.getenv('FLUTTERWAVE_ENCRYPTION_KEY')
FLUTTERWAVE_BASE_URL = os.getenv('FLUTTERWAVE_BASE_URL')



#  When using tools like ngrok, the public URL (e.g., https://your-ngrok-domain.ngrok-free.app) is treated as an external domain. Django needs to explicitly know that this domain is trusted to avoid rejecting requests as potentially harmful.
CSRF_TRUSTED_ORIGINS = [
    ' https://9a2c-102-88-37-35.ngrok-free.app',
]


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


STATIC_ROOT = BASE_DIR / "staticfiles"  # For production (collectstatic)

STATICFILES_DIRS = [
    BASE_DIR / "static",  #used it when you have static files outsit your static folder
]





