import os  # isort:skip

gettext = lambda s: s
"""
Django settings for your project.

Generated by 'django-admin startproject' using Django 1.11.14.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ImproperlyConfigured

# a convenient shortcut to import environment variables
env = os.environ.get
true_values = ['1', 'true', 'y', 'yes', 'on', 1, True]


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(__file__)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
if env('DJANGO_SECRET_KEY'):
    SECRET_KEY = env('DJANGO_SECRET_KEY')
else:
    key_file = os.path.join(BASE_DIR, '.secret_key')
    try:
        from pathlib import Path
        SECRET_KEY = Path(key_file).read_text()
    except (ImportError, FileNotFoundError):
        print("Generating a new SECRET_KEY (just once)")
        from django.core.management.utils import get_random_secret_key
        secret_key = get_random_secret_key()
        Path(key_file).write_text(secret_key)
        SECRET_KEY = Path(key_file).read_text()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DJANGO_DEBUG', 'True').lower() in true_values

# this env is set from the deploy script
if env('DJANGO_ALLOWED_HOSTS_STRING', False):
    ALLOWED_HOSTS = str(env('DJANGO_ALLOWED_HOSTS_STRING')).strip('"').split()
elif DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = ["127.0.0.1", "0.0.0.0", 'localhost']

# Application definition

WSGI_APPLICATION = 'wsgi.application'

ROOT_URLCONF = 'urls'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = env('TIME_ZONE_IDENTIFIER', 'Europe/Zurich')
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static-collected')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings',
                'django_settings_export.settings_export',
                'dynamic_preferences.processors.global_preferences',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader'
            ],
        },
    },
]

MIDDLEWARE = (
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
)

INSTALLED_APPS = (
    # needs to be first to override cms templates
    'usermgmt',
    'custom_user',
    'aldryn_translation_tools',
    'djangocms_modules',
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.redirects',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'filer',
    'easy_thumbnails',
    'djangocms_file',
    'djangocms_icon',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_snippet',
    'djangocms_video',
    'djangocms_maps',
    'djangocms_bootstrap4',
    'djangocms_bootstrap4.contrib.bootstrap4_alerts',
    'djangocms_bootstrap4.contrib.bootstrap4_badge',
    # doesnt allow to configure custom designs, we made our own
    # 'djangocms_bootstrap4.contrib.bootstrap4_card',
    'src.card_columns_plugin',
    'djangocms_bootstrap4.contrib.bootstrap4_carousel',
    'djangocms_bootstrap4.contrib.bootstrap4_collapse',
    'djangocms_bootstrap4.contrib.bootstrap4_content',
    'djangocms_bootstrap4.contrib.bootstrap4_grid',
    'djangocms_bootstrap4.contrib.bootstrap4_jumbotron',
    'djangocms_bootstrap4.contrib.bootstrap4_link',
    'djangocms_bootstrap4.contrib.bootstrap4_listgroup',
    'djangocms_bootstrap4.contrib.bootstrap4_media',
    'djangocms_bootstrap4.contrib.bootstrap4_picture',
    'djangocms_bootstrap4.contrib.bootstrap4_tabs',
    'djangocms_bootstrap4.contrib.bootstrap4_utilities',
    'dynamic_preferences',
    'aldryn_apphooks_config',
    'adminsortable2',
    'parler',
    'gtm',
    # django-filer does not support SVG
    'svg_image_field',
    # nor does the bs4 image field
    'svg_image_plugin',
    'rest_framework',
    'rest_framework.authtoken',
    'djangocms_history',

    # Aldryn forms and dependencies
    # See https://github.com/aldryn/aldryn-forms for documentation
    'absolute',
    'aldryn_forms',
    'aldryn_forms.contrib.email_notifications',
    'emailit',

    # Example PLugins
    # 'src.inline_alignment_plugin',
    # 'src.hide_plugin',
    # 'src.testimonials.apps.TestimonialsApp',
    # 'src.lightbox_gallery_plugin',
    # 'src.float_plugin',

    # aldryn newsblog
    # this is djangocms default blogging system
    # its a bit bloated, and I wonder if it can be used without aldryn_people and aldryn_categories, which would help
    # to reduce complexity.
    # you will probably need to add these
    # 'aldryn_categories',
    # 'aldryn_common',
    # 'aldryn_newsblog',
    # 'aldryn_people',
    # 'sortedm2m',
    # 'taggit',
)

USER_FIELDS = ['email']
AUTH_USER_MODEL = "custom_user.User"

# marked as optional in the doc but seems to be necessary for this setup
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

LANGUAGES = (
    ## Customize this
    ('en', gettext('en')),
)

CMS_LANGUAGES = {
    ## Customize this
    1: [
        {
            'code': 'en',
            'name': gettext('en'),
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },
    ],
    'default': {
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
}

DATE_INPUT_FORMATS = [
    '%d.%m.%Y', '%d.%m.%y',  # European
    '%Y-%m-%d',  # ISO (for native mobile datepickers)
    '%m/%d/%Y', '%m/%d/%y',  # US
    '%d %b %Y', '%d %B %Y',  # some long formats
]

TIME_INPUT_FORMATS = [
    '%H:%M',  # '14:30'
    '%H:%M:%S',  # '14:30:59'
    '%H:%M:%S.%f',  # '14:30:59.000200'
]

DATE_FORMAT = 'j F Y'
TIME_FORMAT = 'H:i'
DATETIME_FORMAT = 'j F Y H:i'
YEAR_MONTH_FORMAT = 'F Y'
MONTH_DAY_FORMAT = 'j F'
SHORT_DATE_FORMAT = 'j N Y'
SHORT_DATETIME_FORMAT = 'j N Y H:i'
FIRST_DAY_OF_WEEK = 1

# email stuff
BUSINESS_NAME = env('BUSINESS_NAME', 'Project Name')
BASE_URL = env('BASE_URL', 'http://localhost:8000')
BUSINESS_EMAIL = env('BUSINESS_EMAIL', 'tech@what.digital')
BUSINESS_EMAIL_VANE = "%(name)s <%(address)s>" % {"name": BUSINESS_NAME, "address": BUSINESS_EMAIL}
DEFAULT_FROM_EMAIL = BUSINESS_EMAIL_VANE
EMAIL_BACKEND = env('EMAIL_BACKEND', 'django.core.mail.backends.dummy.EmailBackend')
EMAIL_HOST = env('EMAIL_HOST', '')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', '')
EMAIL_HOST_USER = env('EMAIL_HOST_USER', '')
EMAIL_PORT = env('EMAIL_PORT', '')
EMAIL_USE_TLS = env('EMAIL_USE_TLS', False)

HTTPS = env('HTTPS', 'false').lower() in true_values

if HTTPS:
    PROTOCOL = 'https'
else:
    PROTOCOL = 'http'

CMS_TEMPLATES = (
    ('main.html', 'Default Template'),
    # static_templates example, remove this
    ('static_templates/home.html', 'Home'),
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

if env('DB_ENGINE') == 'django.db.backends.postgresql':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env('DB_NAME', 'db'),
            'USER': env('DB_USER', 'db'),
            'PASSWORD': env('DB_PASSWORD', 'db'),
            'HOST': env("DB_HOST", 'localhost'),
            'PORT': env("DB_PORT", "5432"),
        },
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        },
    }

MIGRATION_MODULES = {}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

# this is by default set to the value npm start uses in package.json
# for PRODUCTION this value has to be unset! (Set it to False via an env var)
WEBPACK_DEV_BUNDLE_BASE_URL = env('WEBPACK_DEV_BUNDLE_BASE_URL', 'http://localhost:8090/assets/')

STATICFILES_DIRS += (os.path.join(BASE_DIR, 'private'),)

SETTINGS_EXPORT = [
    'WEBPACK_DEV_BUNDLE_BASE_URL',
    'BUSINESS_NAME',
]

CKEDITOR_SETTINGS = {
    'language': '{{ language }}',
    'toolbar': 'CUSTOM',
    # http://ckeditor.com/apps/ckeditor/4.4.0/samples/plugins/toolbar/toolbar.html
    'toolbar_CUSTOM': [
        ['Undo', 'Redo'],
        ['cmsplugins', '-', 'ShowBlocks'],
        ['Format', 'Styles', 'FontSize'],
        # ['Format', 'FontSize'],
        ['TextColor', 'BGColor', '-', 'PasteText', 'PasteFromWord', 'RemoveFormat'],
        ['Maximize', ''],
        '/',
        ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '-', ],
        ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
        # we dont want 'Link', this is done by the bootstrap4 link/button plugin which covers all kind of links
        ['Unlink'],
        ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Table'],
        ['Source']
    ],
    'toolbarCanCollapse': False,
    # All styling-related config is outsourced to static/djangocms_text_ckeditor/js/ckeditor.wysiwyg.js
    # because of https://github.com/aldryn/aldryn-bootstrap3/issues/154
    # https://github.com/divio/django-cms-explorer/blob/908a88afa4e1d1176e267e77eb5c61e31ef0f9e5/static/js/addons/ckeditor.wysiwyg.js#L73
    'stylesSet': 'default:{}/djangocms_text_ckeditor/js/ckeditor.wysiwyg.js'.format(STATIC_URL),
    # 'extraPlugins': 'cmsplugins' // this is already included in 'TextPlugin'
    # NOTE: cms plugins don't work in 'HtmlField', at all!
    # see https://github.com/divio/djangocms-text-ckeditor/issues/317
    # 'contentsCss': 'default:{}/djangocms_text_ckeditor/css/ckeditor.wysiwyg.css'.format(STATIC_URL),
}

CMS_PLACEHOLDER_CONF = {
    None: {
        'excluded_plugins': [],
    },
    'main_content': {
        'name': gettext("Page Content"),
        'excluded_plugins': [],
    },
    'sidebar_right': {
        'name': gettext("Sidebar Right"),
        'excluded_plugins': [],
    },
    'sidebar_left': {
        'name': gettext("Sidebar Left"),
        'excluded_plugins': [],
    },
    'testimonial_content': {
        'name': gettext("Testimonial Page Content"),
        'excluded_plugins': [],
    },
    'newsblog_listing_additional_content': {
        'name': gettext("Additional Blog Listing Page Content"),
        'excluded_plugins': [],
    },

    'newsblog_article_content': {
        'name': gettext("Newsblog Article Content"),
        'excluded_plugins': [],
    },

    'newsblog_social': {
        'name': gettext("Static Blog Article Additional Content"),
        'excluded_plugins': [],
    },
}

#djangocms-bootstrap4
# we use 24 instead of the default 12
DJANGOCMS_BOOTSTRAP4_GRID_SIZE = 24

DJANGOCMS_BOOTSTRAP4_GRID_COLUMN_CHOICES = (
    ('col', _('Column')),
    # for full width columns that have no left and right paddings
    ('col p-0', _('Full-width Column')),
    ('w-100', _('Break')),
    ('', _('Empty'))
)

#djangocms-maps settings
MAPS_PROVIDERS = [
    ('mapbox', _('Mapbox OSM (API key required)')),
]

MAPS_MAPBOX_API_KEY = env('MAPS_MAPBOX_API_KEY', '123')


# available settings with their default values
DYNAMIC_PREFERENCES = {

    # a python attribute that will be added to model instances with preferences
    # override this if the default collide with one of your models attributes/fields
    'MANAGER_ATTRIBUTE': 'preferences',

    # The python module in which registered preferences will be searched within each app
    'REGISTRY_MODULE': 'preferences',

    # Allow quick editing of preferences directly in admin list view
    # WARNING: enabling this feature can cause data corruption if multiple users
    # use the same list view at the same time, see https://code.djangoproject.com/ticket/11313
    'ADMIN_ENABLE_CHANGELIST_FORM': False,

    # Customize how you can access preferences from managers. The default is to
    # separate sections and keys with two underscores. This is probably not a settings you'll
    # want to change, but it's here just in case
    'SECTION_KEY_SEPARATOR': '__',

    # Use this to disable caching of preference. This can be useful to debug things
    'ENABLE_CACHE': True,

    # Use this to disable checking preferences names. This can be useful to debug things
    'VALIDATE_NAMES': True,
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
}


if not DEBUG:
    GTM_CONTAINER_ID = env('GTM_CONTAINER_ID', "GTM-1234")


STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'


INSTALLED_APPS += (
    # ReCaptchaField
    'captcha',  # django-recaptcha
    'aldryn_forms_recaptcha_plugin',
)

RECAPTCHA_PUBLIC_KEY = env('ALDRYN_FORMS_RECAPTCHA_SITE_KEY', '123')
RECAPTCHA_PRIVATE_KEY = env('ALDRYN_FORMS_RECAPTCHA_SECRET', '123')
NOCAPTCHA = True


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', 'file'],
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'DEBUG',
            # https://docs.python.org/3/library/logging.handlers.html
            # because of https://justinmontgomery.com/rotating-logs-with-multiple-workers-in-django
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': env('LOGFILE', os.path.join(BASE_DIR, 'default.log')),
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

ENVIRONMENT = env('DJANGO_ENV', 'develop')
SENTRY_IS_ENABLED = env('SENTRY_IS_ENABLED', 'false').lower() in true_values


if SENTRY_IS_ENABLED:

    import sentry_sdk
    import logging
    from sentry_sdk.integrations.django import DjangoIntegration
    from sentry_sdk.integrations.logging import LoggingIntegration

    # noinspection PyTypeChecker
    sentry_sdk.init(
        dsn="https://123@sentry.io/123",
        integrations=[
            DjangoIntegration(),
            LoggingIntegration(
                level=logging.INFO,  # Capture info and above as breadcrumbs
                event_level=None  # Send no events from log messages
            )
        ],
        environment=ENVIRONMENT,
    )
