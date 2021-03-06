# Generated by Django 3.2.9 on 2021-11-13 14:38

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.TextField(help_text='Descripción de la raza para que los jugadores lo lean')),
                ('fuerza', models.IntegerField(default=0)),
                ('destreza', models.IntegerField(default=0)),
                ('constitucion', models.IntegerField(default=0)),
                ('inteligencia', models.IntegerField(default=0)),
                ('sabiduria', models.IntegerField(default=0)),
                ('carisma', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Raza',
                'verbose_name_plural': 'Razas',
            },
        ),
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuerza', models.IntegerField(default=0)),
                ('destreza', models.IntegerField(default=0)),
                ('constitucion', models.IntegerField(default=0)),
                ('inteligencia', models.IntegerField(default=0)),
                ('sabiduria', models.IntegerField(default=0)),
                ('carisma', models.IntegerField(default=0)),
                ('experiencia', models.PositiveIntegerField(default=0)),
                ('exp_gastada', models.PositiveIntegerField(default=0)),
                ('nombre', models.CharField(max_length=255)),
                ('edad', models.IntegerField(default=20)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='F', max_length=2)),
                ('ojos', models.CharField(default='Marrones', help_text='Color', max_length=20)),
                ('pelo', models.CharField(default='Moreno', help_text='Color', max_length=20)),
                ('altura', models.DecimalField(decimal_places=2, default=Decimal('1.66'), max_digits=3)),
                ('peso', models.PositiveIntegerField(default=70)),
                ('fisico', models.TextField(help_text='Descripción física, incluyendo características  físicas de la mutación.')),
                ('personalidad', models.TextField(help_text='Breve descripción de la personalidad.')),
                ('historia', models.TextField(help_text='Un resumen de la historia de tu personaje.')),
                ('validado', models.BooleanField(default=False)),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('raza', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fichas.raza')),
            ],
            options={
                'verbose_name': 'Ficha',
                'verbose_name_plural': 'Fichas',
            },
        ),
    ]
