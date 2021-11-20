from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from . import serializers

class BookViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = serializers.BooksSerializer.Meta.model.objects.all()
    serializer_class = serializers.BooksSerializer

class LoanBookViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = serializers.LoanBookSerializer.Meta.model.objects.all()
    serializer_class = serializers.LoanBookSerializer