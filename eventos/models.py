from django.db import models
#from usuarios.models import Usuario
from departamento.models import Departamento

# Create your models here.
class Evento( models.Model ):
    codigo = models.CharField(max_length=40)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    direccion = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    disponible = models.BooleanField(default=False)
    rutaLugar = models.CharField(max_length=150)
    calificacionP = models.IntegerField(default=0)
    eliminado = models.BooleanField(default=False)
    idDepartamento = models.ForeignKey(Departamento,on_delete=models.CASCADE)

    class Meta:
        # se ordena de acuerdo a su fecha el mas reciente se posiciona primero
        ordering = ['-fecha']
    
    def deleted(self):
        self.eliminado = True
        self.save()