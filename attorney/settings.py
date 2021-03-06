"""
Django settings for attorney project.
For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped',
    #### default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    #### local dependencies
    'eultheme',
    'downtime',      # required by eultheme even if we aren't using it
    'widget_tweaks',
    #### local apps
    'attorney.apps.admin',
    'attorney.apps.events',
    'attorney.apps.geo',
    'attorney.apps.people',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    # Default processors##############################
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    ##################################################
    "django.core.context_processors.request",
    "eultheme.context_processors.template_settings",
    ### local context processors
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

ROOT_URLCONF = 'attorney.urls'

WSGI_APPLICATION = 'attorney.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Additional locations of static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'sitemedia'),
]


# used with admin_reorder template tag
ADMIN_REORDER = (
    ("events", ('Event')),
    ("people", ('Grantee, GrantorName')),
    ("geo", ('Place',)),
    ("auth", ('Group', 'User')),
)
# import localsettings
# This will override any previously set value
try:
    from localsettings import *
except ImportError:
    import sys
    print >> sys.stderr, '''Settings not defined. Please configure a version
        of localsettings.py for this site. See localsettings.py.dist for
        setup details.'''

# enable django-debug-toolbar if installed
try:
    import debug_toolbar
    INSTALLED_APPS.append('debug_toolbar')
except ImportError:
    pass

# load & configure django_nose if available (only needed for development)
try:
    # NOTE: errors if DATABASES is not configured (in some cases),
    # so this must be done after importing localsettings
    import django_nose
    INSTALLED_APPS.append('django_nose')
    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
    # currently no plugins or extra command line options needed
except ImportError:
    pass