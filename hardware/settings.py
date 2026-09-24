from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-hids%%k#vrmq*1knb5bqeydc)6qc$ps$6hs6fdeiqx#9h=!b8-'

# Iti puyat/development, mabalin a gawiem a True tapno nalakat a makita ti biddut
DEBUG = True

ALLOWED_HOSTS = ['materiales-los-guayos.onrender.com', '127.0.0.1', 'localhost', '*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hardware'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hardware.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR], 
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

WSGI_APPLICATION = 'hardware.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'es-ve'  # Wenno 'es' para iti Español

TIME_ZONE = 'America/Caracas'

USE_I18N = True
USE_TZ = True

# --- CONFIGURACIÓN DE ARCHIVOS ESTÁTICOS Y MEDIA ---

STATIC_URL = '/static/'

# Diretoria a pangbirukan ti Django kadagiti static files ti proyekto
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Kasapulan para iti WhiteNoise ken ti deployment (Render)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Storage para iti WhiteNoise
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Configuración para imágenes subidas desde el Admin (Banners, Productos)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MAILERS = {
    'default': {
        'BACKEND': 'django.core.mail.backends.console.EmailBackend',
    },
}

import os
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_default_superuser(sender, **kwargs):
    if sender.name == 'hardware':  # O el nombre exacto de tu app principal
        from django.contrib.auth import get_user_model
        User = get_user_model()
        
        username = os.environ.get('administracion')
        email = os.environ.get('nowsara14@gmail.com')
        password = os.environ.get('sara,01122009.')
        
        if username and password:
            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(username=username, email=email, password=password)
                print(f"Superusuario '{username}' creado exitosamente.")