"""
Django settings for DjangoDemo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2q)(^dt*w+_eh$y4e!@p*ggv88uz!=xot97737ws*(si(x&4j7'

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
    'bootstrap_toolkit',
    'Demo',
    'demo_app',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)

ROOT_URLCONF = 'DjangoDemo.urls'

WSGI_APPLICATION = 'DjangoDemo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'djangodemo',
        'PASSWORD': 'djangodemo',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = ' /static/'
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
    #os.path.join(BASE_DIR,  '/demo_app/templates'),
)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
BOOTSTRAP_BASE_URL = STATIC_URL + 'bootstrap/'
BOOTSTRAP_CSS_BASE_URL = BOOTSTRAP_BASE_URL + 'css/'
BOOTSTRAP_CSS_URL = BOOTSTRAP_CSS_BASE_URL + 'bootstrap.min.css'
BOOTSTRAP_JS_BASE_URL = BOOTSTRAP_BASE_URL + 'js/'

# Enable for single bootstrap.js file
BOOTSTRAP_JS_URL = BOOTSTRAP_JS_BASE_URL + 'bootstrap.min.js'

# BOOTSTRAP_BASE_URL = 'http://twitter.github.com/bootstrap/assets/'
# BOOTSTRAP_CSS_BASE_URL  = BOOTSTRAP_BASE_URL + 'css/'
# BOOTSTRAP_CSS_URL       = BOOTSTRAP_CSS_BASE_URL + 'bootstrap.css'
# BOOTSTRAP_JS_BASE_URL   = BOOTSTRAP_BASE_URL + 'js/'
#
# # Enable for single bootstrap.js file
# BOOTSTRAP_JS_URL        = BOOTSTRAP_JS_BASE_URL + 'bootstrap.js'