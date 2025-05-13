from django.db import models
from django.core.exceptions import ValidationError

class ResponsableSala(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Sala(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
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

    usuarios = models.ManyToManyField(UsuarioInscrito, related_name='actividades', blank=True)
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE, related_name='actividades')
    sala_principal = models.ForeignKey(Sala, on_delete=models.SET_NULL, null=True, related_name='actividades_principales')
    salas_secundarias = models.ManyToManyField(Sala, blank=True, related_name='actividades_secundarias')

    def __str__(self):
        return self.nombre

    def clean(self):
        super().clean()
        if self.sala_principal and self.salas_secundarias.filter(id=self.sala_principal.id).exists():
            raise ValidationError("Una sala no puede ser a la vez principal y secundaria.")