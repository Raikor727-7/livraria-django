# Create your models here.
from django.db import models


class Autores(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nome_autor = models.TextField()
    nacionalidade = models.TextField(blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'autores'

    def __str__(self):
        return self.nome_autor


class Categorias(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nome_categoria = models.TextField(unique=True)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorias'

    def __str__(self):
        return self.nome_categoria


class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome = models.TextField()
    email = models.TextField(unique=True)
    telefone = models.TextField(blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    data_cadastro = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'
    
    def __str__(self):
        return self.nome


class Editoras(models.Model):
    id_editora = models.AutoField(primary_key=True)
    nome_editora = models.TextField(unique=True)
    endereco = models.TextField(blank=True, null=True)
    telefone = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'editoras'

    def __str__(self):
        return self.nome_editora


class IsbnLivro(models.Model):
    id_isbn = models.AutoField(primary_key=True)
    id_livro = models.OneToOneField('Livros', models.DO_NOTHING, db_column='id_livro')
    codigo_isbn = models.TextField(unique=True)
    data_registro = models.DateField(blank=True, null=True)
    pais_publicacao = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'isbn_livro'

    def __str__(self):
        return self.id_isbn


class ItensVenda(models.Model):
    id_item = models.AutoField(primary_key=True)
    id_venda = models.ForeignKey('Vendas', models.DO_NOTHING, db_column='id_venda', blank=True, null=True)
    id_livro = models.ForeignKey('Livros', models.DO_NOTHING, db_column='id_livro', blank=True, null=True)
    quantidade = models.IntegerField()
    preco_unitario = models.TextField()  # This field type is a guess.   

    class Meta:
        managed = False
        db_table = 'itens_venda'

    def __str__(self):
        return f"Item {self.id_item}"


class Livros(models.Model):
    id_livro = models.AutoField(primary_key=True)
    titulo = models.TextField()
    ano_publicacao = models.IntegerField(blank=True, null=True)
    preco = models.TextField(blank=True, null=True)  # This field type is a guess.
    estoque = models.IntegerField(blank=True, null=True)
    id_editora = models.ForeignKey(Editoras, models.DO_NOTHING, db_column='id_editora', blank=True, null=True)
    id_categoria = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='id_categoria', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'livros'

    def __str__(self):
        return self.titulo


class LivrosAutores(models.Model):
    id_livro_autor = models.AutoField(primary_key=True)
    id_livro = models.ForeignKey(Livros, models.DO_NOTHING, db_column='id_livro')
    id_autor = models.ForeignKey(Autores, models.DO_NOTHING, db_column='id_autor')
    tipo_contribuicao = models.TextField(blank=True, null=True)
    ordem_autoria = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'livros_autores'

    def __str__(self):
        return f"{self.id_autor} - {self.id_livro}" 


class Vendas(models.Model):
    id_venda = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    data_venda = models.DateField(blank=True, null=True)
    valor_total = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'vendas'

    def __str__(self):
        return f"Venda {self.id_venda} - {self.data_venda}" 