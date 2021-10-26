from rest_framework import serializers
from .models import *

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class DigitalMediasSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalMedia
        fields = '__all__'

class AcademicWorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicWork
        fields = '__all__'

class ModelosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = '__all__'

class DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class PeripheralsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peripheral
        fields = '__all__'