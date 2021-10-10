from django.contrib import admin
from .models import Aluno, Professor, Colaborador, Unidade, Livro

#registros via superuser
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Colaborador)
admin.site.register(Unidade)
admin.site.register(Livro)
