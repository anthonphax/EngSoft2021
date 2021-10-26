from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

item_status = (
    ("D", "Disponível"),
    ("I", "Indisponível"),
    ("M", "Em Manutenção"),
    ("A", "Atrasado")
    )

class GlobalUser(models.Model):
    GENDER_CHOICES = (
    ("M", "Masculino"),
    ("F", "Feminino"),
    ("NA", "Outro/Não declarado")
) 

    id = uuid.uuid1().hex
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cpf = models.CharField(
        max_length=255,
        default="000.000.000-00"
    )
    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        default="NA"
    )
    phoneNumber = models.CharField(
        max_length=255,
        default="(00) 00000-0000"
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
        max_length=8,
        default="NA"
    )
    city = models.CharField(
        max_length=105,
        default='NA'
    )

    def __str__(self):
        return self.user.username

class Student(GlobalUser):
    registrationNumber = models.IntegerField(default=0)
    points = models.IntegerField(name="Pontos", default=0)

class Professor(GlobalUser):
    pass