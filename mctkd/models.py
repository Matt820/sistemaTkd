from django.db import models

# Create your models here.
class Sede(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Apoderado(models.Model):
    dni = models.CharField(max_length=15)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    celular = models.CharField(max_length=12, null=True)
    direccion = models.CharField(max_length=100)
    Distrito = models.CharField(max_length=100)
    Provincia = models.CharField(max_length=100)
    Departamento = models.CharField(max_length=100)

    def __str__(self):
        return self.nombres

class Categoria(models.Model):
    categoria_nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.categoria_nombre

class Cinturon(models.Model):
    cinturon_nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.cinturon_nombre
    
class Profesor(models.Model):
    dni = models.CharField(max_length=15)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    celular = models.CharField(max_length=12, null=True)
    foto = models.ImageField(upload_to='profesor_fotos', null=True)
    sexo = models.CharField(max_length=15)
    estado_civil = models.CharField(max_length=15)
    hijos = models.IntegerField()
    direccion = models.CharField(max_length=100)
    Distrito = models.CharField(max_length=100)
    Provincia = models.CharField(max_length=100)
    Departamento = models.CharField(max_length=100)
    cinturon = models.OneToOneField(Cinturon, on_delete=models.CASCADE, null=True, default=1)

    def __str__(self):
        return self.nombres + self.apellidos

class Horario(models.Model):
    turno = models.CharField(max_length=10)
    dia_semana = models.CharField(max_length=10)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, null=True, default=1)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, null=True, default=1)

    def __str__(self):
        return self.id

class Alumno(models.Model):
    dni = models.CharField(max_length=15)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    sexo = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    fecha_inscripcion = models.DateField()
    celular = models.CharField(max_length=12, null=True)
    foto = models.ImageField(upload_to='alumno_fotos', null=True)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, null=True, default=1)
    apoderado = models.ForeignKey(Apoderado, on_delete=models.CASCADE, null=True, default=1)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, default=1)
    cinturon = models.OneToOneField(Cinturon, on_delete=models.CASCADE, null=True, default=1)    
    horario = models.OneToOneField(Horario, on_delete=models.CASCADE, null=True, default=1)

    def __str__(self):
        return self.nombres

class Pension(models.Model):
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()
    alumno = models.OneToOneField(Alumno, on_delete=models.CASCADE, null=True, default=1)

