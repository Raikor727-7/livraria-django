import time
from django.shortcuts import render, get_object_or_404, redirect
from .models import Livros, Editoras, Categorias
from django.contrib import messages

# Create your views here.

def listar_livros(request):
    """
    VIEW: Listar todos os livros
    URL: /livros/lista/
    Função: Exibe todos os livros em uma tabela
    """
    # 1. Buscar TODOS os livros do banco de dados
    livros = Livros.objects.all()
    
    # 2. Renderizar o template passando a lista de livros
    return render(request, 'livros/lista.html', {'livros': livros})


def criar_livro(request):
    """
    VIEW: Criar novo livro
    URL: /livros/criar/
    Métodos: GET (mostrar formulário), POST (processar dados)
    """
    if request.method == 'POST':
        # 📥 CAPTURAR DADOS DO FORMULÁRIO
        titulo = request.POST.get('titulo')
        ano = request.POST.get('ano_publicacao')
        preco = request.POST.get('preco')
        estoque = request.POST.get('estoque')
        id_editora = request.POST.get('id_editora')  # ID da editora selecionada
        id_categoria = request.POST.get('id_categoria')  # ID da categoria selecionada
        
        # ✅ VALIDAÇÃO: Título é obrigatório
        if not titulo:
            messages.error(request, 'Título não pode estar vazio!')
            return render(request, 'livros/formulario.html')
        
        # ✅ VALIDAÇÃO: Ano (se preenchido)
        if ano:  # Se o usuário preencheu o ano
            try:
                ano = int(ano)  # Converter para número
                # Verificar se ano não é futuro
                if ano > time.localtime().tm_year:
                    messages.error(request, 'Ano não pode ser no futuro!')
                    return render(request, 'livros/formulario.html')
            except ValueError:  # Se não for número válido
                messages.error(request, 'Ano deve ser um número!')
                return render(request, 'livros/formulario.html')

        # ✅ VALIDAÇÃO: Preço (se preenchido)
        if preco:
            try:
                preco = float(preco)  # Converter para decimal
                if preco < 0:  # Não pode ser negativo
                    messages.error(request, 'Preço não pode ser negativo!')
                    return render(request, 'livros/formulario.html')
            except ValueError:
                messages.error(request, 'Preço deve ser um número!')
                return render(request, 'livros/formulario.html')
        
        # ✅ VALIDAÇÃO: Estoque (se preenchido)
        if estoque:
            try:
                estoque = int(estoque)  # Converter para inteiro
                if estoque < 0:  # Não pode ser negativo
                    messages.error(request, 'Estoque não pode ser negativo!')
                    return render(request, 'livros/formulario.html')
            except ValueError:
                messages.error(request, 'Estoque deve ser um número!')
                return render(request, 'livros/formulario.html')

        # 🎉 CRIAR O LIVRO NO BANCO DE DADOS
        livro = Livros.objects.create(
            titulo=titulo,
            ano_publicacao=ano,  # Pode ser None se vazio
            preco=preco,         # Pode ser None se vazio
            estoque=estoque,     # Pode ser None se vazio
        )
        
        # 🔗 CONFIGURAR RELACIONAMENTOS (se selecionados)
        if id_editora:
            # Buscar objeto Editora pelo ID e associar ao livro
            livro.id_editora = Editoras.objects.get(id_editora=id_editora)
        if id_categoria:
            # Buscar objeto Categoria pelo ID e associar ao livro
            livro.id_categoria = Categorias.objects.get(id_categoria=id_categoria)

        livro.save()  # Salvar as alterações (relacionamentos)
        messages.success(request, 'Livro criado com sucesso!')
        return redirect('listar_livros')  # Redirecionar para lista
        
    else:
        # 📤 MÉTODO GET: Mostrar formulário vazio
        # Buscar todas editoras e categorias para preencher os selects
        editoras = Editoras.objects.all()
        categorias = Categorias.objects.all()
        return render(request, 'livros/formulario.html', {
            'editoras': editoras,
            'categorias': categorias
        })


def editar_livro(request, id_livro):
    """
    VIEW: Editar livro existente
    URL: /livros/editar/<id_livro>/
    Parâmetro: id_livro - ID do livro a ser editado
    """
    # 🔍 BUSCAR LIVRO PELO ID (ou retornar 404 se não existir)
    livro = get_object_or_404(Livros, id_livro=id_livro)
    
    if request.method == 'GET':
        # 📤 MÉTODO GET: Mostrar formulário com dados atuais
        editoras = Editoras.objects.all()
        categorias = Categorias.objects.all()
        return render(request, 'livros/formulario_editar.html', {
            'livro': livro,           # Livro a ser editado
            'editoras': editoras,     # Todas editoras para select
            'categorias': categorias  # Todas categorias para select
        })
    else:
        # 📥 MÉTODO POST: Processar atualização
        # Capturar todos os campos do formulário
        titulo = request.POST.get('titulo')
        ano = request.POST.get('ano_publicacao')
        preco = request.POST.get('preco')
        estoque = request.POST.get('estoque')
        id_editora = request.POST.get('id_editora')
        id_categoria = request.POST.get('id_categoria')

        # ✅ VALIDAÇÕES (mesmas da criação)
        if not titulo:
            messages.error(request, 'Título não pode estar vazio!')
            return render(request, 'livros/formulario.html')
        
        if ano:
            try:
                ano = int(ano)
                if ano > time.localtime().tm_year:
                    messages.error(request, 'Ano não pode ser no futuro!')
                    return render(request, 'livros/formulario.html')
            except ValueError:
                messages.error(request, 'Ano deve ser um número!')
                return render(request, 'livros/formulario.html')

        if preco:
            try:
                preco = float(preco)
                if preco < 0:
                    messages.error(request, 'Preço não pode ser negativo!')
                    return render(request, 'livros/formulario.html')
            except ValueError:
                messages.error(request, 'Preço deve ser um número!')
                return render(request, 'livros/formulario.html')
        
        if estoque:
            try:
                estoque = int(estoque)
                if estoque < 0:
                    messages.error(request, 'Estoque não pode ser negativo!')
                    return render(request, 'livros/formulario.html')
            except ValueError:
                messages.error(request, 'Estoque deve ser um número!')
                return render(request, 'livros/formulario.html')

        # ✏️ ATUALIZAR TODOS OS CAMPOS DO LIVRO
        livro.titulo = titulo
        livro.ano_publicacao = ano
        livro.preco = preco
        livro.estoque = estoque
        
        # 🔗 ATUALIZAR RELACIONAMENTOS
        if id_editora:
            livro.id_editora = Editoras.objects.get(id_editora=id_editora)
        else:
            livro.id_editora = None  # Remover editora se selecionado "vazio"
            
        if id_categoria:
            livro.id_categoria = Categorias.objects.get(id_categoria=id_categoria)
        else:
            livro.id_categoria = None  # Remover categoria se selecionado "vazio"
            
        livro.save()  # Salvar todas as alterações no banco
        messages.success(request, 'Livro atualizado com sucesso!')
        return redirect('listar_livros')


def excluir_livro(request, id_livro):
    """
    VIEW: Excluir livro com confirmação
    URL: /livros/deletar/<id_livro>/
    """
    # 🔍 BUSCAR LIVRO PELO ID
    livro = get_object_or_404(Livros, id_livro=id_livro)
    
    if request.method == 'POST':
        # ✅ CONFIRMAÇÃO: Excluir livro permanentemente
        livro.delete()
        messages.success(request, 'Livro excluído com sucesso!')
        return redirect('listar_livros')
    else:
        # ❓ MÉTODO GET: Mostrar página de confirmação
        return render(request, 'livros/confirmar_exclusao.html', {'livro': livro})
    

def buscar_livros(request):
    """
    VIEW: Buscar livros por título
    URL: /livros/buscar/
    Parâmetro GET: 'q' - termo de busca
    """
    # 🔍 CAPTURAR TERMO DE BUSCA (ou string vazia se não existir)
    termo_busca = request.GET.get('q', '')
    
    # 📚 FILTRAR LIVROS: título contém o termo (case-insensitive)
    livros = Livros.objects.filter(titulo__icontains=termo_busca)
    
    # 🎯 RENDERIZAR MESMO TEMPLATA DA LISTA, MAS COM RESULTADOS FILTRADOS
    return render(request, 'livros/lista.html', {'livros': livros})


# CRUD EDITORA

def listar_editoras(request):
    editoras = Editoras.objects.all()
    return render(request, 'livros/lista_editoras.html', {'editoras': editoras})

def criar_editora(request):
    if request.method == 'POST':
        nome = request.POST.get('nome_editora')
        # outras validacoes
    else:
        return render(request, 'livros/formulario_editora.html')