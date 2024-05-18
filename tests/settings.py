from pathlib import Path

from django.utils.translation import gettext_lazy as _

DEBUG = True
USE_TZ = True

import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "very-secret"

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "db.sqlite3"}}

ROOT_URLCONF = "tests.urls"

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "django_extensions",
    "allauth_ui",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.github",
    "allauth.socialaccount.providers.facebook",
    "allauth.socialaccount.providers.linkedin",
    "allauth.socialaccount.providers.digitalocean",
    "allauth.socialaccount.providers.wahoo",
    "widget_tweaks",
    "django_browser_reload",
    "debug_toolbar",
]

LOCAL_APPS = ["tests"]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

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

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

LOCALE_PATHS = [
    Path(__file__).parent.parent / "allauth_ui" / "locale",
]
LANGUAGES = (
    ("en-us", _("English")),
    ("es", _("Spanish")),
)

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# INTERNAL_IPS = ["127.0.0.1"]
ALLOWED_HOSTS = ["*"]
SITE_ID = 1
STATIC_URL = "/static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = Path(__file__).parent / "media"

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 1000

# Email settings
EMAIL_BACKEND = os.getenv('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.qq.com')
EMAIL_PORT = os.getenv('EMAIL_PORT', 465)
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', 'ai_future@foxmail.com')
#EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '1371605683@qq.com')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', 'lhtstalemirpjddj')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', False)
EMAIL_USE_SSL = os.getenv('EMAIL_USE_SSL', True)
DEFAULT_FROM_EMAIL = os.getenv('EMAIL_FROM', 'ai_future@foxmail.com')
