from django.db import models
from django.contrib.auth.models import User

class Usuario(User):
    ROLES = (
        ('estudiante', 'Estudiante'),
        ('maestro', 'Maestro'),
        ('admin', 'Administrador'),
    )
    rol = models.CharField(max_length=20, choices=ROLES, default='estudiante')
    es_protegido = models.BooleanField(default=False) 
    def __str__(self):
        return f"{self.first_name} ({self.rol})"


class Servicio(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    responsable_nombre = models.CharField(max_length=150, blank=True)
    responsable_correo = models.EmailField(blank=True)

    def __str__(self):
        return self.nombre


class UbicacionCecytem(models.Model):
    nombre = models.CharField(max_length=150)
    institucion = models.CharField(max_length=150, default="CECyTEM")
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Incidencia(models.Model):
    ESTADOS = (
        ('PENDIENTE', 'Pendiente'),
        ('EN_PROCESO', 'En Proceso'),
        ('RESUELTO', 'Resuelto'),
    )
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='incidencias')
    titulo = models.CharField(max_length=200)
    servicio = models.ForeignKey(Servicio, on_delete=models.SET_NULL, null=True, blank=True)
    problema_relacionado = models.CharField(max_length=200, blank=True)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=200)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='PENDIENTE')
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.estado}"


class Sugerencia(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='sugerencias')
    titulo = models.CharField(max_length=200)
    desarrollo = models.TextField()
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
