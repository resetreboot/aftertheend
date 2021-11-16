from afterend.settings import *

# Edit the secret key and save it as afterend/docker.py before launching the
# docker-compose build

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g(x#u!%p1t+eo(=1d-o2--c19)@lj2n4pal(=b=3nf$!+q@4ea'

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/app/db/db.sqlite3',
    }
}
