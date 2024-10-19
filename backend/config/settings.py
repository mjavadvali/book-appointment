from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = os.environ.get("SECRET_KEY", "your_default_secret_key")  # Provide a default if necessary
DEBUG = os.environ.get("DEBUG", "True") == "True"  # Set DEBUG based on environment variable
# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost").split(",")

ALLOWED_HOSTS = []


CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]

CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:8000',
    'http://localhost:8000',
    'http://localhost:5173',  # Add your Vue.js app's origin here
]
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'rest_framework.authtoken',
    'dj_rest_auth',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',

    'accounts',
    'appointment',

    'corsheaders',

    'django_celery_beat',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', 
    'django.middleware.security.SecurityMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", "postgres"),  
        "USER": os.environ.get("POSTGRES_USER", "postgres"),  
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", ""),
        "HOST": 'db', 
        "PORT": '5432', 
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',  # Use PostgreSQL backend
#         'NAME': os.environ.get("DATABASE_NAME"),     # Retrieves 'hello_django_dev'
#         'USER': os.environ.get("DATABASE_USER"),     # Retrieves 'hello_django'
#         'PASSWORD': os.environ.get("DATABASE_PASSWORD"), # Retrieves 'hello_django'
#         'HOST': os.environ.get("DATABASE_HOST", "db"), # Retrieves 'db' (defaulting to 'db' if not set)
#         'PORT': os.environ.get("DATABASE_PORT", "5432"), # Retrieves '5432' (defaulting to '5432' if not set)
#     }
# }


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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = "/staticfiles/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.parent  / "media"


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'accounts.User'


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication' 
    ],
}


# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:5173",  
# ]


CSRF_TRUSTED_ORIGINS = [
    'chrome-extension://eejfoncpjfgmeleakejdcanedmefagga',
    'http://127.0.0.1:8000',
    'http://localhost:8000',
    'http://localhost:5173',
    'http://localhost:5173/login',
    'ethereum-http://localhost:5173',
    'ethereum-http://localhost:5173',
    
    
]


# CSRF_COOKIE_DOMAIN = None
# CORS_ORIGIN_ALLOW_ALL = True    

# CSRF_COOKIE_HTTPONLY = False  
# CSRF_COOKIE_SAMESITE = 'Lax' 


SITE_ID = 1