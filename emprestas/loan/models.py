import time
import datetime
from datetime import timedelta
from django.db import models
from ..users.models import Student
from ..items.models import Item

class Emprestimo(request):

    def limite_emprestimos(self):
        if self.user == Student:
            if 0 <= Student.points < 75:
                limite = 2
            elif 75 <= Student.points < 150:
                limite = 3
            elif 150 <= Student.points < 300:
                limite = 4
            elif 300 <= Student.points < 600:
                limite = 5
            elif Student.points >= 600:
                limite = 6
        else:
            limite = 10
        return limite

    def __init__(self):
        self.limite = self.limite_emprestimos()
        self.multa = 0.50 #R$

    def pegarItem(self, v_RegistrationNumber, v_codigoItem):
        self.id = v_codigoItem
        self.inscricao = v_RegistrationNumber
        self.dataInicio = datetime.date.today()
        self.dataLimite = dataInicio + timedelta(days = 7)  ## week

    def devolverItem(self, v_codigoItem):
        self.dataDevolucao = datetime.date.today()
        if self.dataDevolucao > self.dataLimite:
            multa = True
        if not(multa):
            self.multa = 0
        print(f""
              f"Data de final = {self.dataLimite}"
              f"Multa = {self.multa}")