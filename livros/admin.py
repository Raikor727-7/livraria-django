from django.contrib import admin

# Register your models here.
from .models import Livros, Editoras, Categorias, Autores, Clientes, LivrosAutores, Vendas

admin.site.register(Livros)
admin.site.register(Editoras)
admin.site.register(Categorias)
admin.site.register(Autores)
admin.site.register(Clientes)
admin.site.register(Vendas)
admin.site.register(LivrosAutores)

