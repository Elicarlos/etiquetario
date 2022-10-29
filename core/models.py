from django.db import models


# Create your models here.
class Base(models.Model):
    criado = models.DateField('Data de criação', auto_add_now=True)
    modificado = models.DateField('Modificado em ', add_now=True)
    ativo = models.BooleanField('Ativo? ', default=True)
    class Meta:
        abstract = True

class TipoCorte(Base):
    descricao = models.CharField()


class Produto(Base):
    descricao = models.CharField('Descricao: 'max_length=100)
    preco = models.DecimalField(digits=8, decimal_places=2)
    imagem = models.ImageField()


