from rest_framework import viewsets
from .models import *
from .serializers import *

class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer

class DigitalMediasViewSet(viewsets.ModelViewSet):
    queryset = DigitalMedia.objects.all()
    serializer_class = DigitalMediasSerializer

class AcademicWorksViewSet(viewsets.ModelViewSet):
    queryset = AcademicWork.objects.all()
    serializer_class = AcademicWorksSerializer

class ModelosViewSet(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModelosSerializer

class DevicesViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DevicesSerializer

class PeripheralsViewSet(viewsets.ModelViewSet):
    queryset = Peripheral.objects.all()
    serializer_class = PeripheralsSerializer