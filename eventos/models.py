from django.db import models
#from usuarios.models import Usuario
from departamento.models import Departamento

# Create your models here.
class Evento( models.Model ):
    codigo = models.CharField(max_length=40)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    direccion = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    disponible = models.BooleanField(default=False)
    rutaLugar = models.CharField(max_length=150)
    calificacionP = models.IntegerField(default=0)
    eliminado = models.BooleanField(default=False)
    id_departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE)

    class Meta:
        # se ordena de acuerdo a su fecha el mas reciente se posiciona primero
        ordering = ['-fecha']
    
    def deleted(self):
        self.eliminado = True
        self.save()

class Imagenes(models.Model):
    imagen = models.ImageField()
    id_evento = models.ForeignKey(Evento,on_delete=models.CASCADE, related_name='imagenes')

"""
class Comentario( models.Model ):
    calificacion = models.IntegerField(default=0)
    descripcion = models.TextField()
    id_evento = models.ForeignKey(Evento, on_delete =models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
"""