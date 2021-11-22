from rest_framework import serializers
from loan import models

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Loans
        fields = '__all__'