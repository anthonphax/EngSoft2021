from django.contrib import admin
from .models import Usuario, Item

#registros via superuser
admin.site.register(Usuario.Aluno)
admin.site.register(Usuario.Professor)
admin.site.register(Usuario.Colaborador)
admin.site.register(Usuario.Unidade)

admin.site.register(Item.Livro)
admin.site.register(Item.MidiaDigital)
admin.site.register(Item.TrabalhoAcademico)
admin.site.register(Item.Modelo)
admin.site.register(Item.Dispositivo)
admin.site.register(Item.Periferico)
