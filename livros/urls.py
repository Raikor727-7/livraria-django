from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.listar_livros, name='listar_livros'),
    path('criar/', views.criar_livro, name='adicionar_livros'),
    path('editar/<int:id_livro>/', views.editar_livro, name='editar_livros'),
    path('buscar/', views.buscar_livros, name='buscar_livros'),
    path('deletar/<int:id_livro>/', views.excluir_livro, name='deletar_livros'),
]