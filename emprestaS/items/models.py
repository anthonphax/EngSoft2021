from django.db import models
import uuid

class Item(models.Model):

    ITEM_STATUS = (
    ("D", "Disponível"),
    ("I", "Indisponível"),
    ("M", "Em Manutenção"),
    ("A", "Atrasado")
    )

    id = uuid.uuid1().hex
    itemName = models.CharField(max_length=255, default="NA")
    # slug = models.SlugField(max_lenth=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    status = models.CharField(
        max_length=255,
        choices=item_status,
        default="D"
    )

class Book(Item):
    author = models.CharField(max_length=50)
    language = models.CharField(max_length=20, default="Português")
    
    def __str__(self):
        return (f'{self.title} {self.author} {self.language}')

class DigitalMedia(Item):
    def __str__(self):
        return self.itemName

class AcademicWork(Book):
    def __str__(self):
        return (f'{self.title} {self.author} {self.language}')

class Modelo(Item):
    def __str__(self):
        return self.itemName

class Device(Item):
    def __str__(self):
        return self.itemName

class Peripheral(Item):
    def __str__(self):
        return self.itemName