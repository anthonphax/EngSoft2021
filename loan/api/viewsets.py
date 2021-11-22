from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from . import serializers
from .. import models

class LoanByUserViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.LoanSerializer

    def get_queryset(self):
        return serializers.LoanSerializer.Meta.model.objects.filter(loan_user=4)

class GetAllLoansViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.LoanSerializer

    queryset = serializers.LoanSerializer.Meta.model.objects.all()