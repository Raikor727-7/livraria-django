from django.urls import path
from . import views

"""
CONFIGURAÇÃO DE URLs DO APP LIVROS
Cada path mapeia uma URL para uma view específica
"""

urlpatterns = [
    # 📚 LISTA: Exibe todos os livros
    path('lista/', views.listar_livros, name='listar_livros'),
    
    # ➕ CRIAÇÃO: Formulário para criar novo livro
    path('criar/', views.criar_livro, name='adicionar_livros'),
    
    # ✏️ EDIÇÃO: Formulário para editar livro existente (com ID)
    path('editar/<int:id_livro>/', views.editar_livro, name='editar_livros'),
    
    # 🔍 BUSCA: Busca livros por título
    path('buscar/', views.buscar_livros, name='buscar_livros'),
    
    # 🗑️ EXCLUSÃO: Confirmação e exclusão de livro (com ID)
    path('deletar/<int:id_livro>/', views.excluir_livro, name='deletar_livros'),

    # lista de todas as editoras
    path('lista_editora/', views.listar_editoras, name='listar_editoras'),

    # criar nova editora
    path('criar_editora/', views.criar_editora, name='adicionar_editora'),

    path('editar_editora/<int:id_editora>/', views.editar_editoras, name='editar_editora'),

    path('excluir_editora/<int:id_editora>/', views.excluir_editora, name='excluir_editora'),

    #lista de categorias
    path('lista_categoria/', views.listar_categorias, name='listar_categorias'),

    path('adicionar_categoria/', views.adicionar_categoria, name='adicionar_categorias'),

    path('excluir_categoria/<int:id_categoria>/', views.excluir_categorias, name='excluir_categoria'),

    #lista autores
    path('lista_autores/', views.listar_autores, name='listar_autores'),

    path('adicionar_autor', views.adicionar_autor, name='adicionar_autor'),

    path('editar_autor/<int:id_autor>/', views.editar_autor, name='editar_autor'),

    path('excluir_autor/<int:id_autor>/', views.excluir_autor, name='excluir_autor'),

]