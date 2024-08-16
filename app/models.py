from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Personagem(models.Model):

    nome = models.CharField(max_length=80, verbose_name="Nome")
    titulo = models.CharField(max_length=80, verbose_name="Título")
    imagem = models.CharField(max_length=300, verbose_name="Imagem")
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
        verbose_name = "Tipo de mecânica"
        verbose_name_plural = "Tipos de mecânica"

    def __str__(self):
        return f'{self.nome}'
    
class Mecanica(models.Model):

    nome = models.CharField(max_length=80, verbose_name="Nome")
    imagem = models.CharField(max_length=300, verbose_name="Imagem")
    descricao = models.CharField(max_length=400, verbose_name="Descrição")
    tipo_de_mecanica = models.ForeignKey(TipoMecanica, on_delete=models.CASCADE, verbose_name="Tipo de mecânica")

    class Meta:
        verbose_name = "Mecânica"
        verbose_name_plural = "Mecânicas"

    def __str__(self):
        return f'{self.nome}'

class Golpe(models.Model):

    nome = models.CharField(max_length=80, verbose_name="Nome")
    imagens = ArrayField(models.CharField(max_length=300), verbose_name="Imagens")
    notacao = models.CharField(max_length=100, verbose_name="Notação")
    dano = models.PositiveIntegerField(verbose_name="Dano")
    punicao = models.BooleanField(verbose_name="É punição?")
    frame_start = models.IntegerField(verbose_name="Frames de início")
    frame_block = models.IntegerField(verbose_name="Frames de bloqueio")
    mecanica = models.ForeignKey(Mecanica, on_delete=models.CASCADE, verbose_name="Mecânica")
    personagem = models.ForeignKey(Personagem, on_delete=models.CASCADE, verbose_name="Personagem")

    class Meta:
        verbose_name = "Golpe"
        verbose_name_plural = "Golpes"

    def __str__(self):
        return f'{self.nome}'
    
class DificuldadeCombo(models.Model):

    nome = models.CharField(max_length=80, verbose_name="Nome")

    class Meta:
        verbose_name = "Dificuldade do combo"
        verbose_name_plural = "Dificuldades do combo"

    def __str__(self):
        return f'{self.nome}'
    
class Combo(models.Model):

    imagens = ArrayField(models.CharField(max_length=120), verbose_name="Imagens")
    notacao = models.CharField(max_length=100, verbose_name="Notação")
    dificuldade = models.ForeignKey(DificuldadeCombo, on_delete=models.CASCADE, verbose_name="Dificuldade")
    numero_golpes = models.PositiveIntegerField(verbose_name="Número de golpes")
    dano = models.PositiveIntegerField(verbose_name="Dano")
    personagem = models.ForeignKey(Personagem, on_delete=models.CASCADE, verbose_name="Personagem")

    class Meta:
        verbose_name = "Combo"
        verbose_name_plural = "Combos"

    def __str__(self):
        return f'{self.notacao}'
    
class JogadorProfissional(models.Model):

    nome = models.CharField(max_length=80, verbose_name="Nome")
    personagem = models.ForeignKey(Personagem, on_delete=models.CASCADE, verbose_name="Personagem")

    class Meta:
        verbose_name = "Jogador profissional"
        verbose_name_plural = "Jogadores profissionais"

    def __str__(self):
        return f'{self.nome}'
    
class Termo(models.Model):

    nome = models.CharField(max_length=80, verbose_name="Nome")
    descricao = models.CharField(max_length=300, verbose_name="Descrição")

    class Meta:
        verbose_name = "Termo"
        verbose_name_plural = "Termos"

    def __str__(self):
        return f'{self.nome}'
    
class Mapa(models.Model):

    nome = models.CharField(max_length=80, verbose_name="Nome")
    imagem = models.CharField(max_length=300, verbose_name="Imagem")

    class Meta:
        verbose_name = "Mapa"
        verbose_name_plural = "Mapas"

    def __str__(self):
        return f'{self.nome}'
    
class PatchNote(models.Model):

    titulo = models.CharField(max_length=80, verbose_name="Título")
    link = models.CharField(max_length=300, verbose_name="Link")

    class Meta:
        verbose_name = "Patch note"
        verbose_name_plural = "Patch notes"

    def __str__(self):
        return f'{self.titulo}'