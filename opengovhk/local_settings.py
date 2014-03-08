from .settings import Base, CustomThemeBase
import re


class Dev(CustomThemeBase, Base):
    DEBUG = True
    TEMPLATE_DEBUG = True
    TASTYPIE_FULL_DEBUG = True

    # FROIDE_THEME = ''

    @property
    def TEMPLATE_LOADERS(self):
        old = super(Dev, self).TEMPLATE_LOADERS
        if self.FROIDE_THEME is not None:
            return (['froide.helper.theme_utils.ThemeLoader'] + old)
        return old

    # @property
    # def INSTALLED_APPS(self):
    #     installed = super(Dev, self).INSTALLED_APPS
    #     if self.FROIDE_THEME is not None:
    #         return installed.default + [self.FROIDE_THEME]
    #     return installed.default

    ############## Site Configuration #########

    # # Make this unique, and don't share it with anybody.
    # SECRET_KEY = 'make_me_unique!!'

    # # Update site information
    # SITE_NAME = 'Froide'
    # SITE_EMAIL = 'info@example.com'
    # SITE_URL = 'http://localhost:8000'
    # SITE_ID = 1

    # ADMINS = (
    #     # ('Your Name', 'your_email@example.com'),
    # )

    # MANAGERS = ADMINS

    # INTERNAL_IPS = ('127.0.0.1',)

    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
    #         'NAME': 'dev.db',                      # Or path to database file if using sqlite3.
    #         'USER': '',                      # Not used with sqlite3.
    #         'PASSWORD': '',                  # Not used with sqlite3.
    #         'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
    #         'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    #     }
    # }

    # # Add real cache
    # CACHES = {
    #    'default': {
    #        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    #        'LOCATION': 'unique-snowflake'
    #    }
    # }

    ############### PATHS ###############

    # GEOIP_PATH = None
    # @property
    # def GEOIP_PATH(self):
    #     return os.path.join(super(Dev, self).PROJECT_ROOT, '..', 'data')

    # Absolute filesystem path to the directory that will hold user-uploaded files.
    # Example: "/home/media/media.lawrence.com/media/"
    # MEDIA_ROOT = os.path.join(PROJECT_ROOT, "..", "files")

    # Sub path in MEDIA_ROOT that will hold FOI attachments
    # FOI_MEDIA_PATH = 'foi'

    # Absolute path to the directory static files should be collected to.
    # Don't put anything in this directory yourself; store your static files
    # in apps' "static/" subdirectories and in STATICFILES_DIRS.
    # Example: "/home/media/media.lawrence.com/static/"
    # STATIC_ROOT = os.path.join(PROJECT_ROOT, "..", "public")

    # Additional locations of static files
    # STATICFILES_DIRS = (
    #     os.path.join(PROJECT_ROOT, "static"),
    # )

    # Additional locations of template files
    # TEMPLATE_DIRS = (
    #     os.path.join(PROJECT_ROOT, "templates"),
    # )


    ########### URLs #################

    # ROOT_URLCONF = 'froide.urls'

    # URL that handles the media served from MEDIA_ROOT. Make sure to use a
    # trailing slash.
    # Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
    # MEDIA_URL = '/files/'

    # URL prefix for static files.
    # Example: "http://media.lawrence.com/static/"

    # URL that handles the static files like app media.
    # Example: "http://media.lawrence.com"
    # STATIC_URL = "/static/"

    # # Use nginx to serve uploads authenticated
    # USE_X_ACCEL_REDIRECT = True
    # X_ACCEL_REDIRECT_PREFIX = '/protected'

    ### URLs that can be translated to a secret value

    # SECRET_URLS = {
    #     "admin": "admin"
    # }

    ######### Backends, Finders, Processors, Classes ####

    # List of finder classes that know how to find static files in
    # various locations.

    # MIDDLEWARE_CLASSES = [
    #     'django.middleware.common.CommonMiddleware',
    #     'djangosecure.middleware.SecurityMiddleware',
    #     'django.contrib.sessions.middleware.SessionMiddleware',
    #     'django.middleware.csrf.CsrfViewMiddleware',
    #     'django.contrib.auth.middleware.AuthenticationMiddleware',
    #     'django.contrib.messages.middleware.MessageMiddleware',
    #     'pagination.middleware.PaginationMiddleware',
    # ]

    ########## I18N and L10N ##################

    # Local time zone for this installation. Choices can be found here:
    # http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
    # although not all choices may be available on all operating systems.
    # On Unix systems, a value of None will cause Django to use the same
    # timezone as the operating system.
    # If running in a Windows environment this must be set to the same as your
    # system time zone.
    # TIME_ZONE = 'Europe/Berlin'
    # USE_TZ = True

    # Language code for this installation. All choices can be found here:
    # http://www.i18nguy.com/unicode/language-identifiers.html
    # LANGUAGE_CODE = 'en-us'


    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    # USE_I18N = True


    # If you set this to False, Django will not format dates, numbers and
    # calendars according to the current locale
    # USE_L10N = True

    # DATE_FORMAT = "d. F Y"
    # SHORT_DATE_FORMAT = "d.m.Y"
    # DATE_INPUT_FORMATS = ("%d.%m.%Y",)
    # SHORT_DATETIME_FORMAT = "d.m.Y H:i"
    # DATETIME_INPUT_FORMATS = ("%d.%m.%Y %H:%M",)
    # TIME_FORMAT = "H:i"
    # TIME_INPUT_FORMATS = ("%H:%M",)

    # Holidays in your country

    # # Change for your own holidays
    # # Format: (month, day)
    # HOLIDAYS = [
    #     (1, 1),  # New Year's Day
    #     (5, 1),  # Labour Day
    #     (10, 3),  # German Unity Day
    #     (12, 25),  # Christmas
    #     (12, 26)  # Second day of Christmas
    # ]

    # # Weekends are non-working days
    # HOLIDAYS_WEEKENDS = True

    # # Holidays are on days offset to easter sunday
    # # This is a list of offsets
    # HOLIDAYS_FOR_EASTER = (0, -2, 1, 39, 50, 60)


    ######### Logging ##########

    # A sample logging configuration.
    # LOGGING = {
    #     'version': 1,
    #     'disable_existing_loggers': True,
    #     'root': {
    #         'level': 'WARNING',
    #         'handlers': [],
    #     },
    #     'filters': {
    #         'require_debug_false': {
    #             '()': 'django.utils.log.RequireDebugFalse'
    #         }
    #     },
    #     'formatters': {
    #         'verbose': {
    #             'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
    #         },
    #     },
    #     'handlers': {
    #         'mail_admins': {
    #             'level': 'ERROR',
    #             'filters': ['require_debug_false'],
    #             'class': 'django.utils.log.AdminEmailHandler'
    #         },
    #         'console': {
    #             'level': 'DEBUG',
    #             'class': 'logging.StreamHandler',
    #         }
    #     },
    #     'loggers': {
    #         'froide': {
    #             'handlers': ['console'],
    #             'propagate': True,
    #             'level': 'DEBUG',
    #         },
    #         'django.request': {
    #             'handlers': ['mail_admins'],
    #             'level': 'ERROR',
    #             'propagate': True,
    #         },
    #         'django.db.backends': {
    #             'level': 'ERROR',
    #             'handlers': ['console'],
    #             'propagate': False,
    #         }
    #     }
    # }


    ######### Security ###########

    # # enable security features for https-deploys
    # CSRF_COOKIE_SECURE = False
    # CSRF_FAILURE_VIEW = 'froide.account.views.csrf_failure'

    # SESSION_COOKIE_AGE = 3628800  # six weeks
    # SESSION_COOKIE_HTTPONLY = True
    # SESSION_COOKIE_SECURE = False

    # Only in production, but don't forget
    # SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
    # ALLOWED_HOSTS = ('example.com',)

    # # Django-Secure options
    # SECURE_FRAME_DENY = True


    ######### South #############

    # SOUTH_TESTS_MIGRATE = False


    ######### Celery #############

    import djcelery
    djcelery.setup_loader()

    # # setup celery differently
    # CELERY_RESULT_BACKEND = "database"
    # CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
    # # Set to false to actually use celery
    CELERY_ALWAYS_EAGER = False

    ######### Haystack ###########

    # Add a real engine like solr
    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
        }
    }

    # HAYSTACK_CONNECTIONS = {
    # 'default': {
    #     'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
    #     'URL': 'http://127.0.0.1:9200/',
    #     'INDEX_NAME': 'haystack',    
    #     }
    # }

    # HAYSTACK_SIGNAL_PROCESSOR = 'celery_haystack.signals.CelerySignalProcessor'

    ########## Froide settings ########

    # # Add the name of your
    # FROIDE_THEME = 'opengovhk'
    # # Add your theme to the top of installed apps
    # INSTALLED_APPS = [FROIDE_THEME] + INSTALLED_APPS

    rec = re.compile

    FROIDE_CONFIG = dict(
        create_new_publicbody=True,
        publicbody_empty=True,
        user_can_hide_web=True,
        public_body_officials_public=True,
        public_body_officials_email_public=False,
        request_public_after_due_days=14,
        payment_possible=True,
        currency="Euro",
        default_law=1,
        search_engine_query="http://www.google.de/search?as_q=%(query)s&as_epq=&as_oq=&as_eq=&hl=en&lr=&cr=&as_ft=i&as_filetype=&as_qdr=all&as_occt=any&as_dt=i&as_sitesearch=%(domain)s&as_rights=&safe=images",
        greetings=[rec(u"Dear (?:Mr\.?|Ms\.? .*?)")],
        closings=[rec(u"Sincerely yours,?")],
        public_body_boosts={},
        dryrun=False,
        dryrun_domain="opengov.hk",
        allow_pseudonym=False,
        doc_conversion_binary=None,  # replace with libreoffice instance
        doc_conversion_call_func=None  # see settings_test for use
    )


    ###### Email ##############

    # Django settings

    # Change to real backend
    # EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
    EMAIL_SUBJECT_PREFIX = '[OpenGov.HK] '
    SERVER_EMAIL = 'admin@opengov.hk'
    DEFAULT_FROM_EMAIL = 'admin@opengov.hk'

    # Official Notification Mail goes through
    # the normal Django SMTP Backend
    EMAIL_HOST = "mail.1000camels.com"
    EMAIL_PORT = 587
    EMAIL_HOST_USER = "admin@opengov.hk"
    EMAIL_HOST_PASSWORD = "2Bhxklvq"
    EMAIL_USE_TLS = False

    # Froide special case settings
    # IMAP settings for fetching mail
    FOI_EMAIL_PORT_IMAP = 993
    FOI_EMAIL_HOST_IMAP = "mail.1000camels.com"
    FOI_EMAIL_ACCOUNT_NAME = "admin@opengov.hk"
    FOI_EMAIL_ACCOUNT_PASSWORD = "2Bhxklvq"
    FOI_EMAIL_USE_SSL = True


    # SMTP settings for setting FoI mail
    # like Django
    FOI_EMAIL_HOST_USER = FOI_EMAIL_ACCOUNT_NAME
    FOI_EMAIL_HOST_FROM = FOI_EMAIL_HOST_USER
    FOI_EMAIL_HOST_PASSWORD = FOI_EMAIL_ACCOUNT_PASSWORD
    FOI_EMAIL_HOST = "mail.1000camels.com"
    FOI_EMAIL_PORT = 587
    FOI_EMAIL_USE_TLS = False
    
    # The FoI Mail can use a different account
    FOI_EMAIL_DOMAIN = "opengov.hk"

    # Custom FOI email sender address:
    # FOI_EMAIL_FUNC = lambda user_name, secret: "%s.%s@%s" % (user_name, secret, FOI_EMAIL_DOMAIN)

    # Is the message you can send from fixed (put custom
    # address in Reply-To header)
    # or can you send from any address you like?
    FOI_EMAIL_FIXED_FROM_ADDRESS = True