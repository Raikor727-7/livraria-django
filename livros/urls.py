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
]