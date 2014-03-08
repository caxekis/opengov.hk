# -*- coding: utf-8 -*-
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


class ThemeHerokuPostmark(OpenGovHK, HerokuPostmark):
    pass


class ThemeHerokuPostmarkS3(OpenGovHK, HerokuPostmarkS3):
    pass


try:
    from .local_settings import *  # noqa
except ImportError:
    pass
