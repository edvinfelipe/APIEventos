from django.db import models
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
    calificacionP = models.DecimalField(max_digits=3,decimal_places=1, default=0)
    contcomment = models.IntegerField(default=0)
    sumcalificacion = models.IntegerField(default=0)
    eliminado = models.BooleanField(default=False)
    idDepartamento = models.ForeignKey(Departamento,on_delete=models.CASCADE)

    class Meta:
        # se ordena de acuerdo a su fecha el mas reciente se posiciona primero
        ordering = ['-fecha']
    
    def deleted(self):
        self.eliminado = True
        self.contcomment = 0
        self.sumcalificacion = 0
        self.calificacionP = 0
        self.save()
    

    def updated(self,calificacion):
        self.contcomment += 1
        self.sumcalificacion += calificacion
        self.calificacionP = self.sumcalificacion/self.contcomment
        self.save()
        print("calificacion"+str(self.calificacionP))
