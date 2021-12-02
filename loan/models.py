from django.db import models
from uuid import uuid4

LOAN_CHOICES = (
    ("E", "Encerrado"),
    ("C", "Pendente"),
    ("A", "Atrasado")
    )

class Loans(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    # loan_date = models.DateField(editable=False)
    # return_date = models.DateField(editable=False)
    loan_status = models.CharField(choices=LOAN_CHOICES, default="I", max_length=1)
    loan_user = models.CharField(max_length=100)
    loan_items = models.JSONField(encoder=None, default=dict)