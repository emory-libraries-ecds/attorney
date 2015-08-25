# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Use this to generate a new key http://www.miniwebtool.com/django-secret-key-generator/
SECRET_KEY = 'SEPxiese&)++%mb19ebhx^u*))e#ufgega^p-#ya$*ea7(w(jb4f-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

# turn on in QA
#ENABLE_BETA_WARNING = True

ALLOWED_HOSTS = ['127.0.0.1']

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'attorney',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': ''
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
     'require_debug_false': {
         '()': 'django.utils.log.RequireDebugFalse'
     }
 },
    'formatters': {
        'basic': {
            'format': '[%(asctime)s] %(levelname)s:%(name)s::%(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S',
         },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'basic'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename' : '/tmp/file.log',
            'formatter': 'basic'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'danowski': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}