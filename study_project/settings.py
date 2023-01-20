"""
Django settings for study_project project.

Generated by 'django-admin startproject' using Django 2.2.15.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd7x_y##5g8*i7g_=**4n#24+=98wbkhl@09_c@zrw8zer!528f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['todoapp01.pythonanywhere.com','localhost','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',

    # Third-party
    # 'crispy_forms',
    # 'allauth',
    # 'allauth.account',
    # 'debug_toolbar', 

    # local
    'todo.apps.ToDoConfig',
    'accounts.apps.AccountsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware', 
]

ROOT_URLCONF = 'study_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'study_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'todoapp01$todo',
        'USER': 'todoapp01',
        'PASSWORD': 'sI1e$rcRa6I_[Inmc%~:',
        'HOST': 'todoapp01.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}

# developing
# DATABASES = {
#     'default':{
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'sqlite3'
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATICFILES_FINDERS = (
#      'django.contrib.staticfiles.finders.FileSystemFinder',
#      'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#      'compressor.finders.CompressorFinder',
# )


LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

AUTH_USER_MODEL = 'accounts.CustomUser'


#heroku

# db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
# DATABASES['default'].update(db_from_env)

# email

EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FROM_EMAIL = 'todoapp01@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'todoapp01@gmail.com'
EMAIL_HOST_PASSWORD = '];0_`.NusWr22f@.mXbc"~*/em`_?hUb.p(t(T+Aw'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# media
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Cloudinary settings for Django.
# CLOUDINARY_STORAGE = {
#   'CLOUD_NAME': 'ddurzxbw0',  
#   'API_KEY': '298863286693199',  
#   'API_SECRET': '89FQ4f9tfmQJwul0i7a60d055Cw',
# }

# Default django media file storage
# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
