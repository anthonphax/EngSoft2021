# coding: utf8
from django.db import models
from django.contrib.auth.models import User
from django.db import models
import json

#modelos de usuários

class Aluno(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    matricula = models.CharField('Número de Matrícula', max_length=8)

    def __str__(self):
        return self.user.username

class Professor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

class Colaborador(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Unidade(models.Model):
    pass #definição da classe admin

#modelos de itens
class Livro(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    language = models.CharField(max_length=20, default="Português")
    slug = models.SlugField(max_length=255, unique=True) #path na url
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title + " " + self.author + " " + self.language)
        
# class ItemList(models.Model):
    #itemList = ["livro", "mídia digital", "trabalho acadêmico", "modelo", "dispositivo", "outro"]   
#     jsonString = json.dumps(itemList)

#     def __repr__(self):
#         return str(self)
        
#     def __list__(self):
#         for key in self.itemList:
#             return self.itemList.key   