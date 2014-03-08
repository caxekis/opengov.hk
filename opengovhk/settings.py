# -*- coding: utf-8 -*-
import os
from froide.settings import Base, ThemeBase, HerokuPostmark, HerokuPostmarkS3  # noqa


class OpenGovHK(ThemeBase):
    FROIDE_THEME = 'opengovhk.theme'

    SITE_NAME = "OpenGov.HK"
    SITE_EMAIL = "foi@opendatahk.com"
    SITE_URL = 'http://localhost:8000'

    SECRET_URLS = {
        "admin": "admin",
    }

    @property
    def INSTALLED_APPS(self):
        installed = super(OpenGovHK, self).INSTALLED_APPS
        installed += [
            # 'foiidea',
            # 'celery_haystack',
            'djcelery_email',
            # 'djangosecure',
            # 'django.contrib.redirects',
            # 'django.contrib.flatpages'
        ]
        return installed

class Dev(OpenGovHK, Base):
    pass




class Production(OpenGovHK, Base):
    DEBUG = False
    TEMPLATE_DEBUG = False
    ALLOWED_HOSTS = ['opengov.hk']
    ALLOWED_HOSTS = ['*'] # temp flexibility

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    STATIC_ROOT = os.path.abspath(os.path.join(PROJECT_ROOT, "..", "public"))

    PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
    STATIC_ROOT = 'staticfiles'
    STATIC_URL = '/static/'

    STATICFILES_DIRS = (
        os.path.join(PROJECT_PATH, 'static'),
    )
    
    CELERY_ALWAYS_EAGER = False
    COMPRESS_ENABLED = False
    COMPRESS_OFFLINE = False


class Heroku(Production):
    ALLOWED_HOSTS = ['*']
    CELERY_ALWAYS_EAGER = False

    @property
    def LOGGING(self):
        logging = super(Heroku, self).LOGGING
        logging['handlers']['console']['stream'] = sys.stdout
        logging['loggers']['django.request']['handlers'] = ['console']
        return logging

class ThemeHerokuPostmark(OpenGovHK, HerokuPostmark):
    pass


class ThemeHerokuPostmarkS3(OpenGovHK, HerokuPostmarkS3):
    pass


try:
    from .local_settings import *  # noqa
except ImportError:
    pass
