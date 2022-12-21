from blogsite.settings import *
SECRET_KEY = 'django-insecure-xx8(&%3(gtb036+wj#blvi6!67x-ag#-cpubur639#7ezjoe!='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

SESSION_COOKIE_SECURE=True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'
STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

SESSION_COOKIE_SECURE=True
SECURE_SSL_REDIRECT=True
CSRF_COOKIE_SECURE=True
SECURE_HSTS_SECONDS=True
SECURE_HSTS_INCLUDE_SUBDOMAINS=True