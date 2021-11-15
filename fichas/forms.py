# python imports
from decimal import Decimal

# django imports
from django import forms
from django.core.exceptions import ValidationError

# project imports
from fichas.models import Raza, Ficha


ESTADISTICAS = (
    ('F', 'Fuerza'),
    ('D', 'Destreza'),
    ('C', 'Constitución'),
    ('I', 'Inteligencia'),
    ('S', 'Sabiduría'),
    ('A', 'Carisma'),
)


class FichaNueva(forms.Form):
    raza = forms.ModelChoiceField(label="Raza", queryset=Raza.objects.all())
    primer_masdos = forms.ChoiceField(label="Primer +2", choices=ESTADISTICAS)
    segundo_masdos = forms.ChoiceField(label="Segundo +2", choices=ESTADISTICAS)
    primer_masuno = forms.ChoiceField(label="Primer +1", choices=ESTADISTICAS)
    segundo_masuno = forms.ChoiceField(label="Segundo +1", choices=ESTADISTICAS)
    menos_uno = forms.ChoiceField(label="-1", choices=ESTADISTICAS)
    nombre = forms.CharField(max_length=255)
    edad = forms.IntegerField(initial=20, min_value=8)
    sexo = forms.ChoiceField(choices=Ficha.SEXO)
    ojos = forms.CharField(max_length=20, initial="Marrones")
    pelo = forms.CharField(max_length=20, initial="Negro")
    altura = forms.DecimalField(max_digits=3, decimal_places=2, initial=Decimal("1.66"))
    peso = forms.IntegerField(initial=70, min_value=10)
    fisico = forms.CharField(widget=forms.Textarea, min_length=10)
    personalidad = forms.CharField(widget=forms.Textarea, min_length=10)
    historia = forms.CharField(widget=forms.Textarea, min_length=10)

    def clean(self):
        cleaned_data = super().clean()
        stats = set()
        for field in ["primer_masdos", "segundo_masdos", "primer_masuno", "segundo_masuno", "menos_uno"]:
            stats.add(cleaned_data.get(field))

        if len(stats) < 5:
            # Hay algún elemento repetido
            raise ValidationError("No se pueden asignar a una misma estadística varios valores.")


class ExperienciaForm(forms.Form):
    caracteristica = forms.ChoiceField(label="Característica a subir", choices=ESTADISTICAS)
