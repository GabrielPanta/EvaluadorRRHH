from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'fake-key'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
     'django.contrib.admin',         # ✅ Necesario para admin
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'evaluador',                    # ✅ Tu app personalizada
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # ✅ requerido
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # ✅ requerido
    'django.contrib.messages.middleware.MessageMiddleware',      # ✅ requerido
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'evaluador_rrhh_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'evaluador/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',  # ✅ requerido por admin
        'django.contrib.auth.context_processors.auth',  # ✅ requerido
        'django.contrib.messages.context_processors.messages',  # ✅ requerido
    ],
        },
    },
]

WSGI_APPLICATION = 'evaluador_rrhh_django.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

