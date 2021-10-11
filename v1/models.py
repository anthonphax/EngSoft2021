# coding: utf8
from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.db import models
import uuid

#modelos de usuários

gender_choices = (
        ("M", "Masculino"),
        ("F", "Feminino"),
        ("NA", "Outro/Não declarado")
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

        def __str__(self):
            return str(self.title + " " + self.author + " " + self.language)

    class MidiaDigital(models.Model): #CD, DVD, pen-drive
        pass

    class TrabalhoAcademico(models.Model): #artigos, monografias 
        pass

    class Modelo(models.Model): #portfólios, mapas, plantas baixas
        pass

    class Dispositivo(models.Model): #projetores, computadores
        pass

    class Periferico(models.Model): #cabos, adaptadores, etc
        pass
            
