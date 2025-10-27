import time
from django.shortcuts import render, get_object_or_404, redirect
from .models import Livros, Editoras, Categorias
from django.contrib import messages
# Create your views here.

# 1. listar_livros - para mostrar todos os livros
def listar_livros(request):
    # 1. Buscar todos os livros do banco
    livros = Livros.objects.all()
    # 3. Renderizar o template com a lista 2. Passar os livros para o template
    return render(request, 'livros/lista.html', {'livros': livros})

# 2. criar_livro - formulário para criar novo livro  
def criar_livro(request):

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        ano = request.POST.get('ano_publicacao')
        preco = request.POST.get('preco')
        estoque = request.POST.get('estoque')
        id_editora = request.POST.get('id_editora')  # ✅ CAPTURAR
        id_categoria = request.POST.get('id_categoria') 
        
        # VALIDAÇÃO TÍTULO
        if not titulo:
            messages.error(request, 'Título não pode estar vazio!')
            return render(request, 'livros/formulario.html')
        
        # VALIDAÇÃO ANO
        if ano:  # se preencheu ano
            try:
                ano = int(ano)
                if ano > time.localtime().tm_year:  # ano não pode ser futuro
                    messages.error(request, 'Ano não pode ser no futuro!')
                    return render(request, 'livros/formulario.html')
            except ValueError:
                messages.error(request, 'Ano deve ser um número!')
                return render(request, 'livros/formulario.html')

        # VALIDAÇÃO PREÇO
        if preco:  # se preencheu preço
            try:
                preco = float(preco)
                if preco < 0:
                    messages.error(request, 'Preço não pode ser negativo!')
                    return render(request, 'livros/formulario.html')
            except ValueError:
                messages.error(request, 'Preço deve ser um número!')
                return render(request, 'livros/formulario.html')
        
        # VALIDAÇÃO ESTOQUE
        if estoque:  # se preencheu estoque
            try:
                estoque = int(estoque)
                if estoque < 0:
                    messages.error(request, 'Estoque não pode ser negativo!')
                    return render(request, 'livros/formulario.html')
            except ValueError:
                messages.error(request, 'Estoque deve ser um número!')
                return render(request, 'livros/formulario.html')

        # ✅ SÓ AQUI CRIA O LIVRO
        livro = Livros.objects.create(
            titulo=titulo,
            ano_publicacao=ano,
            preco=preco,
            estoque=estoque,
        )
        
        if id_editora:
            livro.id_editora = Editoras.objects.get(id_editora=id_editora)
        if id_categoria:
            livro.id_categoria = Categorias.objects.get(id_categoria=id_categoria)

        livro.save()
        messages.success(request, 'Livro criado com sucesso!')
        return redirect('listar_livros')
        
    else:
        editoras = Editoras.objects.all()
        categorias = Categorias.objects.all()
        return render(request, 'livros/formulario.html', {
            'editoras': editoras,
            'categorias': categorias
        })
        # ⚠️ O que colocar aqui para mostrar o formulário?
    
# 3. editar_livro - formulário para editar livro existente
def editar_livro(request, id_livro):
    livro = get_object_or_404(Livros, id_livro=id_livro)
    
    if request.method == 'GET':
        # ✅ PASSAR EDITORAS E CATEGORIAS PARA O TEMPLATE
        editoras = Editoras.objects.all()
        categorias = Categorias.objects.all()
        return render(request, 'livros/formulario_editar.html', {
            'livro': livro,
            'editoras': editoras,
            'categorias': categorias
        })
    else:
         # ✅ CAPTURAR TODOS OS CAMPOS
        titulo = request.POST.get('titulo')
        ano = request.POST.get('ano_publicacao')
        preco = request.POST.get('preco')
        estoque = request.POST.get('estoque')
        id_editora = request.POST.get('id_editora')
        id_categoria = request.POST.get('id_categoria')

        # VALIDAÇÃO TÍTULO
        if not titulo:
            messages.error(request, 'Título não pode estar vazio!')
            return render(request, 'livros/formulario.html')
        
        # VALIDAÇÃO ANO
        if ano:  # se preencheu ano
            try:
                ano = int(ano)
                if ano > time.localtime().tm_year:  # ano não pode ser futuro
                    messages.error(request, 'Ano não pode ser no futuro!')
                    return render(request, 'livros/formulario.html')
            except ValueError:
                messages.error(request, 'Ano deve ser um número!')
                return render(request, 'livros/formulario.html')

        # VALIDAÇÃO PREÇO
        if preco:  # se preencheu preço
            try:
                preco = float(preco)
                if preco < 0:
                    messages.error(request, 'Preço não pode ser negativo!')
                    return render(request, 'livros/formulario.html')
            except ValueError:
                messages.error(request, 'Preço deve ser um número!')
                return render(request, 'livros/formulario.html')
        
        # VALIDAÇÃO ESTOQUE
        if estoque:  # se preencheu estoque
            try:
                estoque = int(estoque)
                if estoque < 0:
                    messages.error(request, 'Estoque não pode ser negativo!')
                    return render(request, 'livros/formulario.html')
            except ValueError:
                messages.error(request, 'Estoque deve ser um número!')
                return render(request, 'livros/formulario.html')


        # ✅ ATUALIZAR TODOS OS CAMPOS
        livro.titulo = titulo  # ✅ FALTAVA ISSO!
        livro.ano_publicacao = ano
        livro.preco = preco
        livro.estoque = estoque
        
        if id_editora:
            livro.id_editora = Editoras.objects.get(id_editora=id_editora)
        else:
            livro.id_editora = None
            
        if id_categoria:
            livro.id_categoria = Categorias.objects.get(id_categoria=id_categoria)
        else:
            livro.id_categoria = None
            
        livro.save()
        messages.success(request, 'Livro atualizado com sucesso!')
        return redirect('listar_livros')
    # 4. Como redirecionar para a lista?

#  4. excluir_livro - confirmar e excluir livro
def excluir_livro(request, id_livro):
    livro = get_object_or_404(Livros, id_livro=id_livro)
    if request.method == 'POST':
        livro.delete()
        messages.success(request, 'Livro excluído com sucesso!')
        return redirect('listar_livros')
    else:
         return render(request, 'livros/confirmar_exclusao.html', {'livro': livro})
    
def buscar_livros(request):
    termo_busca = request.GET.get('q', '')
    # Como filtrar livros pelo título?
    livros = Livros.objects.filter(titulo__icontains=termo_busca)
    # livros = Livros.objects.filter(???)
    return render(request, 'livros/lista.html', {'livros': livros})