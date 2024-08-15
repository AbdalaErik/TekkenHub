from django.db import models

# Create your models here.

class Personagem(models.Model):

    imagem = models.CharField(max_length=120, verbose_name="Imagem")
    nome = models.CharField(max_length=80, verbose_name="Nome")
    titulo = models.CharField(max_length=80, verbose_name="Título")
    estilo = models.CharField(max_length=80, verbose_name="Estilo de luta")
    pais = models.CharField(max_length=40, verbose_name="País")
    dlc = models.BooleanField(verbose_name="É DLC?")
    resumo = models.CharField(max_length=120, verbose_name="Resumo")
    guias = models.CharField(max_length=400, verbose_name="Guias")

    class Meta:
        verbose_name = "Personagem"
        verbose_name_plural = "Personagens"

    def __str__(self):
        return f'{self.nome}'
    
class TipoMecanica(models.Model):

    nome = models.CharField(max_length=80, verbose_name="Nome")

    class Meta:
        verbose_name = "Tipo de Mecânica"
        verbose_name_plural = "Tipos de Mecânica"

    def __str__(self):
        return f'{self.nome}'
    
class Mecanica(models.Model):

    nome = models.CharField(max_length=80, verbose_name="Nome")
    imagem = models.CharField(max_length=120, verbose_name="Imagem")
    descricao = models.CharField(max_length=400, verbose_name="Descrição")

    class Meta:
        verbose_name = "Mecânica"
        verbose_name_plural = "Mecânicas"

    def __str__(self):
        return f'{self.nome}'
    
class Golpes()