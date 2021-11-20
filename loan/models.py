from django.db import models
from uuid import uuid4

class Loans(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    loan_date = models.DateField()
    return_date = models.DateField()
    loan_status = models.CharField(max_length=10)
    loan_user = models.CharField(max_length=100)