from django.contrib import admin

# Register your models here.
from .models import Livros, Editoras, Categorias, Autores, Clientes, LivrosAutores, Vendas

"""
REGISTRO DE MODELOS NO ADMIN DJANGO
Cada modelo registrado aparece na interface administrativa
"""

# 📚 Registrar todos os modelos para aparecerem no admin
admin.site.register(Livros)        # Livros
admin.site.register(Editoras)      # Editoras  
admin.site.register(Categorias)    # Categorias
admin.site.register(Autores)       # Autores
admin.site.register(Clientes)      # Clientes
admin.site.register(Vendas)        # Vendas
admin.site.register(LivrosAutores) # Relação Livros-Autores