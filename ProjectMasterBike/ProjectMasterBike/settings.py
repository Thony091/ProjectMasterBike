from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# Configuración de la base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'MasterBikeDB',
        'USER': 'masterbike',
        'PASSWORD': os.getenv('DB_PASSWORD', 'projectmasterbike'),
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Configuración de autenticación
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

# Configuración de internacionalización
LANGUAGE_CODE = 'es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Configuración de archivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Configuración de Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'

# Redirección después de iniciar y cerrar sesión
LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'

# Configuración de modelo de usuario personalizado
# AUTH_USER_MODEL = 'core.Usuario'

# Configuración de hosts permitidos
ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # Reemplaza 'your-domain.com' con tu dominio o dirección IP
SECRET_KEY = 'django-insecure-h7o8@gt3@9ye1ab)%t%o2!u2og&4phir827n%8l)+r3*l8*6x!'

# Solo establece DEBUG en False si estás en un entorno de producción seguro
DEBUG = True

# Configuración de middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de aplicaciones
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'rest_framework',
    'crispy_forms',
    'crispy_bootstrap5',
    'core',
    'rest_producto',
    'seguridad',
    'rest_framework.authtoken',
]

# Configuración de templates
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

ROOT_URLCONF = 'ProjectMasterBike.urls'
WSGI_APPLICATION = 'ProjectMasterBike.wsgi.application'
