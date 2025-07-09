from django.db import models

class Candidato(models.Model):
    nombre = models.CharField(max_length=100)
    experiencia = models.IntegerField()
    habilidades = models.TextField()
    estudios = models.CharField(max_length=100)
    personalidad = models.CharField(max_length=100)
    es_elegible = models.BooleanField(default=False)

    @property
    def lista_habilidades(self):
        return [h.strip() for h in self.habilidades.split(',')]


