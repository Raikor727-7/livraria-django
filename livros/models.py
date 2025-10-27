# Create your models here.
from django.db import models

"""
MODELOS DO SISTEMA LIVRARIA
Cada classe representa uma tabela no banco de dados
managed=False significa que as tabelas já existem no banco
"""

class Autores(models.Model):
    """Modelo para armazenar informações dos autores dos livros"""
    id_autor = models.AutoField(primary_key=True)  # Chave primária automática
    nome_autor = models.TextField()  # Nome do autor (obrigatório)
    nacionalidade = models.TextField(blank=True, null=True)  # Opcional
    data_nascimento = models.DateField(blank=True, null=True)  # Opcional
    biografia = models.TextField(blank=True, null=True)  # Opcional

    class Meta:
        managed = False  # Não gerencia criação de tabela (já existe no BD)
        db_table = 'autores'  # Nome da tabela no banco

    def __str__(self):
        """Representação em string do objeto (aparece no admin)"""
        return self.nome_autor


class Categorias(models.Model):
    """Modelo para categorias de livros (ex: Romance, Ficção, etc)"""
    id_categoria = models.AutoField(primary_key=True)
    nome_categoria = models.TextField(unique=True)  # Nome único
    descricao = models.TextField(blank=True, null=True)  # Descrição opcional

    class Meta:
        managed = False
        db_table = 'categorias'

    def __str__(self):
        return self.nome_categoria


class Clientes(models.Model):
    """Modelo para cadastro de clientes da livraria"""
    id_cliente = models.AutoField(primary_key=True)
    nome = models.TextField()  # Nome obrigatório
    email = models.TextField(unique=True)  # Email único
    telefone = models.TextField(blank=True, null=True)  # Opcional
    endereco = models.TextField(blank=True, null=True)  # Opcional
    data_cadastro = models.DateField(blank=True, null=True)  # Opcional

    class Meta:
        managed = False
        db_table = 'clientes'
    
    def __str__(self):
        return self.nome


class Editoras(models.Model):
    """Modelo para editoras dos livros"""
    id_editora = models.AutoField(primary_key=True)
    nome_editora = models.TextField(unique=True)  # Nome único
    endereco = models.TextField(blank=True, null=True)
    telefone = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'editoras'

    def __str__(self):
        return self.nome_editora


class IsbnLivro(models.Model):
    """Modelo para informações ISBN dos livros (relação 1:1 com Livros)"""
    id_isbn = models.AutoField(primary_key=True)
    # Relação um-para-um: cada livro tem um ISBN único
    id_livro = models.OneToOneField('Livros', models.DO_NOTHING, db_column='id_livro')
    codigo_isbn = models.TextField(unique=True)  # Código ISBN único
    data_registro = models.DateField(blank=True, null=True)
    pais_publicacao = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'isbn_livro'

    def __str__(self):
        return f"ISBN {self.id_isbn}"


class ItensVenda(models.Model):
    """Modelo para itens de venda (produtos vendidos)"""
    id_item = models.AutoField(primary_key=True)
    # Relação muitos-para-um: várias vendas podem ter vários itens
    id_venda = models.ForeignKey('Vendas', models.DO_NOTHING, db_column='id_venda', blank=True, null=True)
    id_livro = models.ForeignKey('Livros', models.DO_NOTHING, db_column='id_livro', blank=True, null=True)
    quantidade = models.IntegerField()  # Quantidade vendida
    preco_unitario = models.TextField()  # Preço na hora da venda

    class Meta:
        managed = False
        db_table = 'itens_venda'

    def __str__(self):
        return f"Item {self.id_item}"


class Livros(models.Model):
    """
    MODELO PRINCIPAL - Livros
    Contém todos os dados dos livros e relacionamentos
    """
    id_livro = models.AutoField(primary_key=True)
    titulo = models.TextField()  # Título obrigatório
    ano_publicacao = models.IntegerField(blank=True, null=True)  # Ano opcional
    preco = models.TextField(blank=True, null=True)  # Preço opcional
    estoque = models.IntegerField(blank=True, null=True)  # Estoque opcional
    
    # RELACIONAMENTOS: Um livro pertence a uma editora e uma categoria
    id_editora = models.ForeignKey(Editoras, models.DO_NOTHING, db_column='id_editora', blank=True, null=True)
    id_categoria = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='id_categoria', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'livros'

    def __str__(self):
        """Mostra o título do livro no admin e em outros lugares"""
        return self.titulo


class LivrosAutores(models.Model):
    """
    Modelo de junção para relação muitos-para-muitos
    Um livro pode ter vários autores, um autor pode ter vários livros
    """
    id_livro_autor = models.AutoField(primary_key=True)
    # Relação muitos-para-muitos através desta tabela intermediária
    id_livro = models.ForeignKey(Livros, models.DO_NOTHING, db_column='id_livro')
    id_autor = models.ForeignKey(Autores, models.DO_NOTHING, db_column='id_autor')
    tipo_contribuicao = models.TextField(blank=True, null=True)  # Ex: Autor principal, Coautor
    ordem_autoria = models.IntegerField(blank=True, null=True)  # Ordem dos autores

    class Meta:
        managed = False
        db_table = 'livros_autores'

    def __str__(self):
        return f"{self.id_autor} - {self.id_livro}"


class Vendas(models.Model):
    """Modelo para registrar vendas realizadas"""
    id_venda = models.AutoField(primary_key=True)
    # Relação: uma venda pertence a um cliente
    id_cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    data_venda = models.DateField(blank=True, null=True)  # Data da venda
    valor_total = models.TextField(blank=True, null=True)  # Valor total da venda

    class Meta:
        managed = False
        db_table = 'vendas'

    def __str__(self):
        return f"Venda {self.id_venda} - {self.data_venda}"