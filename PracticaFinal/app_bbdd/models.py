from django.db import models

# Create your models here.
from django.db import models

class ResponsableSala(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Sala(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.PositiveIntegerField()
    ubicacion = models.CharField(max_length=100)
    responsable = models.OneToOneField(ResponsableSala, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Monitor(models.Model):
    nombre = models.CharField(max_length=100)
    especializacion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class UsuarioInscrito(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    horario = models.DateTimeField()
    descripcion = models.TextField()
    duracion = models.PositiveIntegerField(help_text="Duración en minutos")
    plazas_disponibles = models.PositiveIntegerField()

    # Relaciones:
    usuarios = models.ManyToManyField(UsuarioInscrito, related_name='actividades')
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE, related_name='actividades')
    sala_principal = models.ForeignKey(Sala, on_delete=models.SET_NULL, null=True, related_name='actividades_principales')
    salas_secundarias = models.ManyToManyField(Sala, blank=True, related_name='actividades_secundarias')

    def __str__(self):
        return self.nombre
