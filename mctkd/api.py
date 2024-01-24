from .models import Sede, Apoderado, Categoria, Cinturon, Profesor, Horario, Alumno, Pension
from rest_framework import viewsets, permissions
from .serializers import SedeSerializer, ApoderadoSerializer, CategoriaSerializer, CinturonSerializer, ProfesorSerializer, AlumnoSerializer, HorarioSerializer, PensionSerializer

class SedeViewSet(viewsets.ModelViewSet):
    queryset = Sede.objects.all()
    permission_classes = [permissions.AllowAny] #se puede colocar autenticacion
    serializer_class = SedeSerializer


class ApoderadoViewSet(viewsets.ModelViewSet):
    queryset = Apoderado.objects.all()
    permission_classes = [permissions.AllowAny] #se puede colocar autenticacion
    serializer_class = ApoderadoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    permission_classes = [permissions.AllowAny] #se puede colocar autenticacion
    serializer_class = CategoriaSerializer

class CinturonViewSet(viewsets.ModelViewSet):
    queryset = Cinturon.objects.all()
    permission_classes = [permissions.AllowAny] #se puede colocar autenticacion
    serializer_class = CinturonSerializer

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    permission_classes = [permissions.AllowAny] #se puede colocar autenticacion
    serializer_class = ProfesorSerializer

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    permission_classes = [permissions.AllowAny] #se puede colocar autenticacion
    serializer_class = HorarioSerializer

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    permission_classes = [permissions.AllowAny] #se puede colocar autenticacion
    serializer_class = AlumnoSerializer

class PensionViewSet(viewsets.ModelViewSet):
    queryset = Pension.objects.all()
    permission_classes = [permissions.AllowAny] #se puede colocar autenticacion
    serializer_class = PensionSerializer