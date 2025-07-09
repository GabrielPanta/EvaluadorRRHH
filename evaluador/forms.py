from django import forms
from .models import Candidato
from .models import Puesto, Postulacion

class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = ['nombre', 'experiencia', 'habilidades', 'estudios', 'personalidad']

class PuestoForm(forms.ModelForm):
    class Meta:
        model = Puesto
        fields = '__all__'

class PostulacionForm(forms.ModelForm):
    class Meta:
        model = Postulacion
        fields = ['candidato', 'puesto']