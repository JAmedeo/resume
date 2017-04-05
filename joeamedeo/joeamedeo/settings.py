"""
Django settings for joeamedeo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd=^95vi&$^kt!2wf*+yuu5257r^7+6y9381u9wj4anandwfaww'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'japp',
    'rest_framework',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.gzip.GZipMiddleware',
)

ROOT_URLCONF = 'joeamedeo.urls'

WSGI_APPLICATION = 'joeamedeo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ja_db',
        'USER': 'ja_db',
        'PASSWORD': 'jAdBPass3179',
        'HOST':'web353.webfaction.com',
        'PORT': '5432',
    }
}
'''
DATABASES = {

}
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/home/jamedeo/webapps/joeamedeo_static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
    os.path.join(BASE_DIR, 'japp/static/'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates/'),
    os.path.join(BASE_DIR,  'japp/templates/'),
)

#EMAIL_HOST = 'smtp.webfaction.com'
#EMAIL_HOST_USER = 'mailbox_username'
#EMAIL_HOST_PASSWORD = 'mailbox_password'
#DEFAULT_FROM_EMAIL = 'valid_email_address'
#SERVER_EMAIL = 'valid_email_address'


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGE_SIZE': 10
}