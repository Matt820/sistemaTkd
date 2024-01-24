from rest_framework import serializers
from .models import Sede, Apoderado, Categoria, Cinturon, Profesor, Horario, Alumno, Pension

class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = ('id','nombre', 'direccion', 'telefono')
        read_only_fields = ('id', ) #campo que no se permitira modificar

class ApoderadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apoderado
        fields = ('id','dni', 'nombres', 'celular', 'apellidos', 'celular', 'direccion', 'Distrito', 'Provincia', 'Departamento')
        read_only_fields = ('id', ) #campo que no se permitira modificar

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'categoria_nombre')
        read_only_fields = ('id', ) #campo que no se permitira modificar

class CinturonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinturon
        fields = ('id', 'cinturon_nombre')
        read_only_fields = ('id', ) #campo que no se permitira modificar

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ('id', 'dni', 'nombres', 'apellidos', 'fecha_nacimiento', 'celular', 'foto', 'sexo', 'estado_civil', 'hijos', 'direccion', 'Distrito', 'Provincia', 'Departamento', 'cinturon', )
        read_only_fields = ('id', ) #campo que no se permitira modificar

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = ('id', 'turno', 'dia_semana', 'hora_inicio', 'hora_fin', 'sede', 'profesor', )
        read_only_fields = ('id', ) #campo que no se permitira modificar
    
class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ('id', 'dni', 'nombres', 'apellidos', 'sexo', 'fecha_nacimiento', 'fecha_inscripcion', 'celular', 'foto', 'sede', 'apoderado', 'categoria', 'cinturon', 'horario', )
        read_only_fields = ('id', ) #campo que no se permitira modificar    

class PensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pension
        fields = ('id', 'monto', 'fecha_pago', 'alumno')
        read_only_fields = ('id', ) #campo que no se permitira modificar