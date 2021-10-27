from rest_framework import viewsets
from .models import Student, Professor, Collaborator, UnityUser
from .serializers import StudentSerializer, ProfessorSerializer, CollaboratorSerializer, UnityUserSerializer


class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class CollaboratorViewSet(viewsets.ModelViewSet):
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorSerializer


class UnityUserViewSet(viewsets.ModelViewSet):
    queryset = UnityUser.objects.all()
    serializer_class = UnityUserSerializer
