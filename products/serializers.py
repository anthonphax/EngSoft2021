from rest_framework import serializers
from .models import *

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class DigitalMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalMedia
        fields = '__all__'

class AcademicWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicWork
        fields = '__all__'

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class PeripheralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peripheral
        fields = '__all__'