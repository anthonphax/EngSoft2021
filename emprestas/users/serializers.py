from rest_framework import serializers
from .models import Student, Professor, Collaborator, UnityUser


class UnityUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnityUser
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'


class CollaboratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborator
        fields = '__all__'
