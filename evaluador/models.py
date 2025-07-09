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


class Puesto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    requisitos = models.TextField(help_text="Habilidades requeridas separadas por coma")
    experiencia_minima = models.IntegerField()
    estado = models.CharField(
        max_length=10,
        choices=[('abierto', 'Abierto'), ('cerrado', 'Cerrado')],
        default='abierto'
    )

    def __str__(self):
        return self.titulo
    

class Postulacion(models.Model):
    candidato = models.ForeignKey("Candidato", on_delete=models.CASCADE)
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)
    fecha_postulacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidato.nombre} - {self.puesto.titulo}"