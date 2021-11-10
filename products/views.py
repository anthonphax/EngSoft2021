from rest_framework import viewsets
from .models import *
from .serializers import *

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DigitalMediaViewSet(viewsets.ModelViewSet):
    queryset = DigitalMedia.objects.all()
    serializer_class = DigitalMediaSerializer

class AcademicWorkViewSet(viewsets.ModelViewSet):
    queryset = AcademicWork.objects.all()
    serializer_class = AcademicWorkSerializer

class ModeloViewSet(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer

# class DeviceSerializerViewSet(viewsets.ModelViewSet):
#     queryset = DeviceSerializer.objects.all()
#     serializer_class = DeviceSerializerSerializer

class PeripheralViewSet(viewsets.ModelViewSet):
    queryset = Peripheral.objects.all()
    serializer_class = PeripheralSerializer