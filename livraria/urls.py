"""
URL configuration for livraria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include  # include para incluir URLs de outros apps

urlpatterns = [
    # 🏠 ADMIN: Interface administrativa do Django
    path('admin/', admin.site.urls),
    
    # 📚 APP LIVROS: Inclui todas as URLs definidas em livros/urls.py
    # Todas URLs começarão com /livros/
    path('livros/', include('livros.urls')),
]