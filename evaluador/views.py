from django.shortcuts import render, redirect
from .models import Candidato
from .forms import CandidatoForm
from pyswip import Prolog
import os
import pandas as pd
from django.conf import settings
from .models import Candidato
from django.shortcuts import get_object_or_404
from .models import Puesto, Postulacion, Candidato
from .forms import PuestoForm, PostulacionForm
from django.shortcuts import render, redirect

def generar_logica_prolog():
    ruta = os.path.join(settings.BASE_DIR, 'evaluador', 'logica.pl')
    with open(ruta, 'w') as f:
        f.write('% Generado automáticamente\n\n')
        for c in Candidato.objects.all():
            nombre = c.nombre.lower().replace(" ", "_")
            f.write(f"experiencia({nombre}, {c.experiencia}).\n")
            for h in c.habilidades.split(","):
                f.write(f"habilidad({nombre}, {h.strip()}).\n")
        f.write("""

elegible(Nombre) :-
    experiencia(Nombre, Exp),
    Exp >= 2,
    habilidad(Nombre, programacion),
    habilidad(Nombre, trabajo_en_equipo).
perfil_tecnico(Nombre) :-
    habilidad(Nombre, programacion),
    experiencia(Nombre, Exp),
    Exp >= 2.

perfil_liderazgo(Nombre) :-
    habilidad(Nombre, liderazgo),
    experiencia(Nombre, Exp),
    Exp >= 1.

junior(Nombre) :- experiencia(Nombre, Exp), Exp < 2.
semisenior(Nombre) :- experiencia(Nombre, Exp), Exp >= 2, Exp < 4.
senior(Nombre) :- experiencia(Nombre, Exp), Exp >= 4.

perfil_integral(Nombre) :-
    habilidad(Nombre, programacion),
    habilidad(Nombre, trabajo_en_equipo),
    habilidad(Nombre, liderazgo),
    experiencia(Nombre, Exp),
    Exp >= 3.

sobresaliente(Nombre) :-
    experiencia(Nombre, Exp),
    Exp >= 5,
    habilidad(Nombre, programacion),
    habilidad(Nombre, trabajo_en_equipo),
    habilidad(Nombre, liderazgo).

necesita_formacion(Nombre) :-
    \\+ habilidad(Nombre, programacion).
""")


def evaluar_candidato(nombre):
    prolog = Prolog()
    prolog.consult("evaluador/logica.pl") 
    nombre = nombre.lower().replace(" ", "_")  
    result = list(prolog.query(f"elegible({nombre})"))
    return len(result) > 0

def ver_perfiles(request):
    prolog = Prolog()
    prolog.consult("evaluador/logica.pl")

    perfiles = {
        "perfil_tecnico": list(prolog.query("perfil_tecnico(Nombre)")),
        "perfil_liderazgo": list(prolog.query("perfil_liderazgo(Nombre)")),
        "perfil_integral": list(prolog.query("perfil_integral(Nombre)")),
        "sobresaliente": list(prolog.query("sobresaliente(Nombre)")),
        "necesita_formacion": list(prolog.query("necesita_formacion(Nombre)"))
    }

    
    for key in perfiles:
        perfiles[key] = [p["Nombre"] for p in perfiles[key]]

    return render(request, "evaluador/perfiles.html", {"perfiles": perfiles})



def index(request):
    candidatos = Candidato.objects.all()
    resultados = [(c, evaluar_candidato(c.nombre)) for c in candidatos]
    return render(request, 'evaluador/index.html', {'resultados': resultados})


def agregar_candidato(request):
    if request.method == 'POST':
        form = CandidatoForm(request.POST)
        if form.is_valid():
            candidato = form.save(commit=False)
            candidato.es_elegible = evaluar_candidato(candidato.nombre)
            candidato.save()
            generar_logica_prolog() 
            return redirect('/')
    else:
        form = CandidatoForm()
    return render(request, 'evaluador/formulario.html', {'form': form})



def editar_candidato(request, id):
    candidato = get_object_or_404(Candidato, id=id)
    if request.method == 'POST':
        form = CandidatoForm(request.POST, instance=candidato)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CandidatoForm(instance=candidato)
    return render(request, 'evaluador/formulario.html', {'form': form, 'editar': True})

def eliminar_candidato(request, id):
    candidato = get_object_or_404(Candidato, id=id)
    candidato.delete()
    return redirect('/')


def crear_puesto(request):
    if request.method == 'POST':
        form = PuestoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_puestos')
    else:
        form = PuestoForm()
    return render(request, 'evaluador/crear_puesto.html', {'form': form})


def listar_puestos(request):
    puestos = Puesto.objects.filter(estado='abierto')
    return render(request, 'evaluador/puestos.html', {'puestos': puestos})


def postular_puesto(request,puesto_id):
    if request.method == 'POST':
        form = PostulacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_puestos')
    else:
        form = PostulacionForm()
    return render(request, 'evaluador/postular.html', {'form': form})

def ver_postulaciones(request):
    postulaciones = Postulacion.objects.select_related('candidato', 'puesto').all()
    return render(request, 'evaluador/postulaciones.html', {'postulaciones': postulaciones})

def resumen_candidatos(request):
    candidatos = Candidato.objects.all()

   
    data = []
    for c in candidatos:
        data.append({
            'Nombre': c.nombre,
            'Experiencia': c.experiencia,
            'Habilidades': ', '.join([h.strip() for h in c.habilidades.split(',')])
        })

    df = pd.DataFrame(data)

  
    resumen = df['Experiencia'].describe().to_dict() if not df.empty else {}

    return render(request, 'evaluador/resumen.html', {
        'resumen': resumen,
        'total_candidatos': len(df)
    })