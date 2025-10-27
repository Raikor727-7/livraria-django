📚 DOCUMENTAÇÃO COMPLETA - SISTEMA LIVRARIA DJANGO
🎯 VISÃO GERAL DO PROJETO
Sistema de gerenciamento de livraria desenvolvido em Django com funcionalidades completas de CRUD (Create, Read, Update, Delete) para livros, incluindo relacionamentos com editoras e categorias.

🏗️ ARQUITETURA DO PROJETO
Estrutura de Diretórios
text
livraria-django/
├── livraria/                 # Configurações do projeto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── livros/                   # App principal
│   ├── migrations/
│   ├── templates/livros/
│   │   ├── lista.html
│   │   ├── formulario.html
│   │   ├── formulario_editar.html
│   │   └── confirmar_exclusao.html
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── data/
│   └── livraria.db          # Banco de dados SQLite
└── manage.py
📊 MODELOS DE DADOS
Livros (Modelo Principal)
id_livro - Chave primária automática

titulo - Título do livro (obrigatório)

ano_publicacao - Ano de publicação (opcional)

preco - Preço do livro (opcional)

estoque - Quantidade em estoque (opcional)

id_editora - Relacionamento com Editoras (ForeignKey)

id_categoria - Relacionamento com Categorias (ForeignKey)

Outros Modelos
Autores - Informações dos autores

Editoras - Dados das editoras

Categorias - Categorias de livros

Clientes - Cadastro de clientes

Vendas - Registro de vendas

LivrosAutores - Relação muitos-para-muitos entre livros e autores

🔄 FLUXO DO CRUD COMPLETO
1. CREATE (Criar Livro)
URL: /livros/criar/

GET: Exibe formulário com selects para editora e categoria

POST: Valida dados e cria novo livro no banco

Validações: Título obrigatório, ano não pode ser futuro, preço/estoque não negativos

2. READ (Listar/Buscar Livros)
URLs:

/livros/lista/ - Lista todos os livros

/livros/buscar/ - Busca livros por título (case-insensitive)

3. UPDATE (Editar Livro)
URL: /livros/editar/<id_livro>/

GET: Formulário preenchido com dados atuais

POST: Atualiza livro com novas informações

4. DELETE (Excluir Livro)
URL: /livros/deletar/<id_livro>/

GET: Página de confirmação com dados do livro

POST: Exclui permanentemente o livro

🎨 INTERFACES (TEMPLATES)
lista.html
Tabela com todos os livros

Formulário de busca

Links para editar/excluir cada livro

Botão "Adicionar Novo Livro"

Sistema de mensagens (sucesso/erro)

formulario.html (Criação)
Campos: título, ano, preço, estoque

Selects para editora e categoria

Validação HTML5 (required)

formulario_editar.html (Edição)
Similar ao de criação, mas com valores preenchidos

Selects com opção selecionada atual

confirmar_exclusao.html
Exibe dados do livro para confirmação

Botão de confirmação (vermelho) e cancelar

⚙️ CONFIGURAÇÕES TÉCNICAS
Settings Principais
python
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': r'C:\PROJETOS\Python\livraria django\data\livraria.db',
    }
}

# Apps Instaladas
INSTALLED_APPS = [
    'livros',  # Seu app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
URLs Configuradas
Projeto (livraria/urls.py):

python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('livros/', include('livros.urls')),  # Inclui URLs do app
]
App (livros/urls.py):

python
urlpatterns = [
    path('lista/', views.listar_livros, name='listar_livros'),
    path('criar/', views.criar_livro, name='adicionar_livros'),
    path('editar/<int:id_livro>/', views.editar_livro, name='editar_livros'),
    path('buscar/', views.buscar_livros, name='buscar_livros'),
    path('deletar/<int:id_livro>/', views.excluir_livro, name='deletar_livros'),
]
🔧 FUNCIONALIDADES IMPLEMENTADAS
Validações de Dados
Título: Campo obrigatório

Ano: Não pode ser futuro, deve ser número válido

Preço: Não pode ser negativo, deve ser número

Estoque: Não pode ser negativo, deve ser número inteiro

Sistema de Busca
Busca por título usando icontains (case-insensitive)

Campo mantém valor após busca

Link para limpar busca

Relacionamentos
Selects dinâmicos para Editora e Categoria

Valores pré-selecionados na edição

Campos opcionais (pode ser None)

Feedback ao Usuário
Mensagens de sucesso (verde)

Mensagens de erro (validações)

Confirmação antes de excluir

🚀 COMO USAR O SISTEMA
1. Acessar o Sistema
text
python manage.py runserver
Acesse: http://localhost:8000/livros/lista/

2. Operações Disponíveis
Ver Livros: Acesse a lista principal

Adicionar: Clique em "Adicionar Novo Livro"

Buscar: Use o campo de busca na lista

Editar: Clique em "Editar" em qualquer livro

Excluir: Clique em "Excluir" e confirme

3. Admin Django
Acesse http://localhost:8000/admin/ para gerenciamento avançado de todos os modelos.

💡 MELHORIAS FUTURAS SUGERIDAS
1. CRUDs Adicionais
python
# Implementar para:
- Autores
- Editoras  
- Categorias
- Clientes
2. Buscas Avançadas
python
# Filtros combinados:
- Por autor
- Por editora
- Por categoria
- Por faixa de ano
- Por faixa de preço
3. Testes Automatizados
python
# Exemplo de testes a implementar:
- test_criar_livro_valido
- test_buscar_livro_por_titulo
- test_editar_livro_existente
- test_excluir_livro
- test_validacoes_campos_obrigatorios
4. Melhorias de UX
Paginação na lista de livros

Ordenação por colunas

Confirmação antes de sair do formulário sem salvar

Upload de capas de livros

🛠️ COMANDOS ÚTEIS
Desenvolvimento
bash
# Executar servidor
python manage.py runserver

# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser
Manutenção
bash
# Verificar erros
python manage.py check

# Shell interativo
python manage.py shell
✅ CHECKLIST DE FUNCIONALIDADES
CRUD completo para Livros

Relacionamentos (Editora, Categoria)

Validações de dados

Sistema de busca

Interface responsiva

Mensagens de feedback

Admin Django configurado

URLs nomeadas

Templates organizados

CRUD para outros modelos

Testes automatizados

Buscas avançadas

