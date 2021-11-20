from django.db import models
from uuid import uuid4

class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_date = models.DateField()
    publisher = models.CharField(max_length=255)
    totalQuantity = models.IntegerField(default=0)
    availableQuantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)