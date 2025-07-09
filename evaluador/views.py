from django.shortcuts import render, redirect
from .models import Candidato
from .forms import CandidatoForm
from pyswip import Prolog
import os
from django.conf import settings
from .models import Candidato
from django.shortcuts import get_object_or_404

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
""")

# ✅ Usamos esta función para conectarnos con Prolog
def evaluar_candidato(nombre):
    prolog = Prolog()
    prolog.consult("evaluador/logica.pl")  # Asegúrate que este archivo existe y tiene la regla elegible(Nombre).
    nombre = nombre.lower().replace(" ", "_")  # ¡clave!
    result = list(prolog.query(f"elegible({nombre})"))
    return len(result) > 0

# Vista principal
def index(request):
    candidatos = Candidato.objects.all()
    resultados = [(c, evaluar_candidato(c.nombre)) for c in candidatos]
    return render(request, 'evaluador/index.html', {'resultados': resultados})

# Vista para agregar candidatos
def agregar_candidato(request):
    if request.method == 'POST':
        form = CandidatoForm(request.POST)
        if form.is_valid():
            candidato = form.save(commit=False)
            candidato.es_elegible = evaluar_candidato(candidato.nombre)
            candidato.save()
            generar_logica_prolog()  # 🔁 Actualiza el archivo logica.pl
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

