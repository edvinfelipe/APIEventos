from django.db import models
from usuarios.models import Usuario

# Create your models here.
class Evento( models.Model ):
    lugar = models.CharField(max_length=150)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    disponible = models.BooleanField(default=False)
    rutaAfiche = models.CharField(max_length=100)
    rutaLugar = models.CharField(max_length=100)

    class Meta:
        # se ordena de acuerdo a su fecha el mas reciente se posiciona primero
        ordering = ['-fecha']

class Comentario( models.Model ):
    descripcion = models.TextField()
    id_evento = models.ForeignKey(Evento, on_delete =models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)