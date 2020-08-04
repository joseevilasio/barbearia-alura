from django.db import models

class Produto(models.Model):
    nome_produto = models.CharField(max_length=200)
    descricao_produto = models.CharField(max_length=400)
    preco_produto = models.DecimalField(max_digits=5, decimal_places=2)
    foto_produto = models.ImageField(upload_to='fotos/', blank=True)

    def __str__(self):
        return self.nome_produto


class Contatos(models.Model):
    nome = models.CharField(max_length=300)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    mensagem = models.TextField()
    contato = models.CharField(max_length=10)
    turno_atendimento = models.CharField(max_length=10)
    newsletter = models.BooleanField(default=False)


