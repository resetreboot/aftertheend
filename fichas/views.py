# django imports
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

# project imports
from fichas.models import Ficha
from fichas.forms import FichaNueva, ExperienciaForm


# Create your views here.
def procesar_puntos(data):
    """
    Dado los datos limpios de un form, nos da la ficha
    """
    rels = {
        "F": "fuerza",
        "D": "destreza",
        "C": "constitucion",
        "I": "inteligencia",
        "S": "sabiduria",
        "A": "carisma"
    }
    stats = {
        "fuerza": 0,
        "destreza": 0,
        "constitucion": 0,
        "inteligencia": 0,
        "sabiduria": 0,
        "carisma": 0
    }

    stats[rels[data["primer_masdos"]]] = 2
    stats[rels[data["segundo_masdos"]]] = 2
    stats[rels[data["primer_masuno"]]] = 1
    stats[rels[data["segundo_masuno"]]] = 1
    stats[rels[data["menos_uno"]]] = -1

    return stats


@login_required()
def index(request):
    fichas = Ficha.objects.filter(jugador=request.user)
    context = {"fichas": fichas}

    return render(request, 'index.html', context)


@login_required()
def ficha_view(request, ficha_id):
    ficha = get_object_or_404(Ficha, id=ficha_id, jugador=request.user)
    context = {"ficha": ficha}

    return render(request, 'ficha.html', context)


@login_required()
def experiencia(request, ficha_id):
    ficha = get_object_or_404(Ficha, id=ficha_id, jugador=request.user)
    context = {}

    if request.method == "POST":
        form = ExperienciaForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            if ficha.experiencia - ficha.exp_gastada < settings.EXPERIENCE_POINTS:
                context["error"] = "Insuficientes puntos de experiencia."

            else:
                car = data["caracteristica"]
                ficha.exp_gastada += settings.EXPERIENCE_POINTS

                if car == "F":
                    ficha.fuerza += 1

                elif car == "D":
                    ficha.destreza += 1

                elif car == "C":
                    ficha.constitucion += 1

                elif car == "I":
                    ficha.inteligencia += 1

                elif car == "S":
                    ficha.sabiduria += 1

                elif car == "A":
                    ficha.carisma += 1

                ficha.save()

    else:
        form = ExperienciaForm()

    context["form"] = form
    context["ficha"] = ficha
    # Only show the form if there's enough experience to buy points
    context["show_form"] = ficha.experiencia - ficha.exp_gastada >= settings.EXPERIENCE_POINTS

    return render(request, 'experiencia.html', context)


@login_required()
def new(request):
    if request.method == "POST":
        form = FichaNueva(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            puntos = procesar_puntos(data)
            nueva_ficha = Ficha(
                jugador=request.user,
                raza=data["raza"],
                fuerza=puntos["fuerza"],
                destreza=puntos["destreza"],
                constitucion=puntos["constitucion"],
                inteligencia=puntos["inteligencia"],
                sabiduria=puntos["sabiduria"],
                carisma=puntos["carisma"],
                nombre=data["nombre"],
                edad=data["edad"],
                sexo=data["sexo"],
                ojos=data["ojos"],
                pelo=data["pelo"],
                altura=data["altura"],
                peso=data["peso"],
                fisico=data["fisico"],
                personalidad=data["personalidad"],
                historia=data["historia"],
            )
            nueva_ficha.save()
            return HttpResponseRedirect('/')

    else:
        form = FichaNueva()

    return render(request, 'nueva.html', {"form": form})
