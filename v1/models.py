# coding: utf8
from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.db import models
import uuid

gender_choices = (
        ("M", "Masculino"),
        ("F", "Feminino"),
        ("NA", "Outro/Não declarado")
    ) 

item_status = (
    ("D", "Disponível"),
    ("I", "Indisponível"),
    ("M", "Em Manutenção"),
    ("A", "Atrasado")
    )

class Usuario:
    class Aluno(models.Model): #todos os modelos são classes python que herdam a classe models
        id = uuid.uuid1().hex #32
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        matricula = models.CharField('Número de Matrícula', max_length=8)
        cpf = models.CharField(max_length=11, default="0")
        gender = models.CharField(
            max_length=20,
            choices = gender_choices,
            default="NA"
        )
        telefone = models.CharField(
            max_length=11,
            default=0
            )
        address1 = models.CharField(
            "Endereço, linha 1",
            max_length=255,
            default="NA"
        )
        address2 = models.CharField(
            "Endereço, linha 2",
            max_length=255,
            default="NA"
        )
        cep = models.CharField(
            "CEP",
            max_length=9,
            default="NA"
        )
        city = models.CharField(
            max_length=105,
            default="NA"
            )
        points = models.IntegerField(
            name="Pontos",
            default=0
        )

        def level(self): #game
            if self.points < 75:
                return 1
            elif 75 >= self.points < 150:
                print("in training")
                return 2
            elif 150 >= self.points < 300:
                print("gear")
                return 3
            elif 600 >= self.points < 600:
                print("machine")
                return 4
            elif self.points >= 600:
                print("veteran")
                return 5
            else:
                print("algo errado")

        def __str__(self):
            return self.user.username

    class Professor(models.Model):
        id = uuid.uuid1().hex #32
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        cpf = models.CharField(max_length=11, default="0")
        gender = models.CharField(
            max_length=20,
            choices = gender_choices,
            default="NA"
        )
        telefone = models.CharField(
            max_length=11,
            default=0
            )
        address1 = models.CharField(
            "Endereço, linha 1",
            max_length=255,
            default="NA"
        )
        address2 = models.CharField(
            "Endereço, linha 2",
            max_length=255,
            default="NA"
        )
        cep = models.CharField(
            "CEP",
            max_length=9,
            default="NA"
        )
        city = models.CharField(
            max_length=105,
            default="NA"
            )
        
        def __str__(self):
            return self.user.username

    class Colaborador(models.Model):
        id = uuid.uuid1().hex #32
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        cpf = models.CharField(max_length=11, default="0")
        gender = models.CharField(
            max_length=20,
            choices = gender_choices,
            default="NA"
        )
        telefone = models.CharField(
            max_length=11,
            default=0
            )
        address1 = models.CharField(
            "Endereço, linha 1",
            max_length=255,
            default="NA"
        )
        address2 = models.CharField(
            "Endereço, linha 2",
            max_length=255,
            default="NA"
        )
        cep = models.CharField(
            "CEP",
            max_length=9,
            default="NA"
        )
        city = models.CharField(
            max_length=105,
            default="NA"
            )

        def __str__(self):
            return self.user.username

    class Unidade(models.Model):  #administrador do sistema
        id = uuid.uuid1().hex #32
        cnpj = models.CharField(max_length=14, default="0")
        telefone = models.CharField(
            max_length=11, 
            default=0
            )
        address1 = models.CharField(
            "Endereço, linha 1",
            max_length=255,
            default="NA"
        )
        address2 = models.CharField(
            "Endereço, linha 2",
            max_length=255,
            default="NA"
        )
        cep = models.CharField(
            "CEP",
            max_length=9,
            default="NA"
        )
        city = models.CharField(
            max_length=105,
            default="NA"
            )

class Item:
    class Livro(models.Model):
        id = uuid.uuid1().hex #32
        title = models.CharField(max_length=255)
        author = models.CharField(max_length=50)
        language = models.CharField(max_length=20, default="Português")
        slug = models.SlugField(max_length=255, unique=True) #path na url
        description = models.TextField()
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        status = models.CharField(
            max_length=255,
            choices=item_status,
            default="D"
        )

        def __str__(self):
            return str(self.title + " " + self.author + " " + self.language)

    class MidiaDigital(models.Model): #CD, DVD, pen-drive
        id = uuid.uuid1().hex
        title = models.CharField(max_length=255) 
        slug = models.SlugField(max_length=255, unique=True)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        description = models.TextField()
        status = models.CharField(
            max_length=255,
            choices=item_status,
            default="D"
        )

    class TrabalhoAcademico(models.Model): #artigos, monografias 
        id = uuid.uuid1().hex
        title = models.CharField(max_length=255)
        author = models.CharField(max_length=50) 
        slug = models.SlugField(max_length=255, unique=True)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        description = models.TextField()
        status = models.CharField(
            max_length=255,
            choices=item_status,
            default="D"
        )

    class Modelo(models.Model): #portfólios, mapas, plantas baixas
        id = uuid.uuid1().hex
        title = models.CharField(max_length=255)
        slug = models.SlugField(max_length=255, unique=True)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        description = models.TextField()
        status = models.CharField(
            max_length=255,
            choices=item_status,
            default="D"
        )
    class Dispositivo(models.Model): #projetores, computadores
        id = uuid.uuid1().hex
        title = models.CharField(max_length=255)
        slug = models.SlugField(max_length=255, unique=True)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        description = models.TextField() 
        status = models.CharField(
            max_length=255,
            choices=item_status,
            default="D"
        )
    class Periferico(models.Model): #cabos, adaptadores, etc
        id = uuid.uuid1().hex
        title = models.CharField(max_length=255)
        slug = models.SlugField(max_length=255, unique=True)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        description = models.TextField()
        status = models.CharField(
            max_length=255,
            choices=item_status,
            default="D"
        )

    def emprestimo(self):
        pass

    def devolucao(self):
        # if self.status != "A":
        #     self.points += 5
        #     self.status = "D"
        # else:
        #     self.status = "D"
        pass
    def manutencao(self):
        pass 
            
class Relatorio:
    class Demanda(models.Model):
        pass
    class Estoque(models.Model):
        pass
    class Danos(models.Model):
        pass
    class Previsão(models.Model):
        pass