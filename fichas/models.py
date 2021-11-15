# python imports
from decimal import Decimal

# django imports
from django.conf import settings
from django.db import models


# Create your models here.

class Raza(models.Model):
    nombre = models.CharField(max_length=40, null=False)
    descripcion = models.TextField(help_text="Descripción de la raza para que los jugadores lo lean")
    # Estadísticas
    fuerza = models.IntegerField(default=0)
    destreza = models.IntegerField(default=0)
    constitucion = models.IntegerField(default=0)
    inteligencia = models.IntegerField(default=0)
    sabiduria = models.IntegerField(default=0)
    carisma = models.IntegerField(default=0)

    def __str__(self):
        return f"Raza: {self.nombre}"

    class Meta:
        verbose_name = "Raza"
        verbose_name_plural = "Razas"


class Ficha(models.Model):
    # Constantes
    SEXO = [
        ("M", "Masculino"),
        ("F", "Femenino"),
    ]
    # Estadísticas
    fuerza = models.IntegerField(default=0)
    destreza = models.IntegerField(default=0)
    constitucion = models.IntegerField(default=0)
    inteligencia = models.IntegerField(default=0)
    sabiduria = models.IntegerField(default=0)
    carisma = models.IntegerField(default=0)
    # Evolucion
    experiencia = models.PositiveIntegerField(default=0)
    exp_gastada = models.PositiveIntegerField(default=0)
    # Biografía
    jugador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    raza = models.ForeignKey(Raza, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=255, null=False)
    edad = models.IntegerField(default=20)
    sexo = models.CharField(max_length=2, choices=SEXO, null=False, default="F")
    ojos = models.CharField(max_length=20, default="Marrones", help_text="Color")
    pelo = models.CharField(max_length=20, default="Moreno", help_text="Color")
    altura = models.DecimalField(max_digits=3, decimal_places=2, default=Decimal("1.66"))
    peso = models.PositiveIntegerField(default=70)
    fisico = models.TextField(help_text="Descripción física, incluyendo características  físicas de la mutación.")
    personalidad = models.TextField(help_text="Breve descripción de la personalidad.")
    historia = models.TextField(help_text="Un resumen de la historia de tu personaje.")
    validado = models.BooleanField(default=False)

    def __str__(self):
        return f"Ficha de {self.nombre} de {self.jugador.first_name}({self.jugador.username})"

    class Meta:
        verbose_name = "Ficha"
        verbose_name_plural = "Fichas"
