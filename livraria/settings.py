"""
Django settings for livraria project.
Configurações principais do projeto Django
"""

from pathlib import Path

# 📁 CAMINHO BASE DO PROJETO
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 CONFIGURAÇÕES DE SEGURANÇA
SECRET_KEY = 'django-insecure-%)u&!-6+xd1_h0!nl=s9o*_fs9+mj6v255^ugpzr&6c#aa_oqk'
DEBUG = True  # ❗ MUDAR PARA False EM PRODUÇÃO
ALLOWED_HOSTS = []  # 🌐 Hosts permitidos (vazio = todos em desenvolvimento)

# 📦 APPS INSTALADOS
INSTALLED_APPS = [
    'livros',  # ✅ SEU APP - Sempre colocar primeiro
    'django.contrib.admin',      # 🏠 Admin do Django
    'django.contrib.auth',       # 🔐 Autenticação
    'django.contrib.contenttypes', # 📋 Sistema de tipos de conteúdo
    'django.contrib.sessions',   # 💾 Sessões
    'django.contrib.messages',   # 💬 Sistema de mensagens
    'django.contrib.staticfiles', # 🖼️ Arquivos estáticos
]

# 🔧 MIDDLEWARES (processadores de requisição)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # 🔒 Proteção CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',  # 💬 Mensagens
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 🌐 CONFIGURAÇÃO DE URLs PRINCIPAL
ROOT_URLCONF = 'livraria.urls'

# 🎨 CONFIGURAÇÃO DE TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # 📁 Diretórios adicionais de templates
        'APP_DIRS': True,  # ✅ Procura templates dentro de cada app
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',  # 💬 Mensagens
            ],
        },
    },
]

# 🚀 CONFIGURAÇÃO WSGI (para deploy)
WSGI_APPLICATION = 'livraria.wsgi.application'

# 🗄️ CONFIGURAÇÃO DO BANCO DE DADOS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # 📊 SQLite (desenvolvimento)
        'NAME': r'C:\PROJETOS\Python\livraria django\data\livraria.db',  # 📁 Caminho do BD
    }
}

# 🔐 VALIDAÇÕES DE SENHA
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🌍 INTERNACIONALIZAÇÃO
LANGUAGE_CODE = 'en-us'  # 🈴 Idioma
TIME_ZONE = 'UTC'        # ⏰ Fuso horário
USE_I18N = True          # 🌐 Internacionalização
USE_TZ = True            # ⏰ Usar timezone

# 🖼️ ARQUIVOS ESTÁTICOS (CSS, JS, imagens)
STATIC_URL = 'static/'

# 🔑 CHAVE PRIMÁRIA PADRÃO
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'