from django.db import models

# Create your models here.
class Localidad( models.Model ):
    tipo = models.CharField(max_length=45)
    costo = models.DecimalField(max_digits=8, decimal_places= 4)
    cantidadAsientos = models.IntegerField()
    canitidadAsientosDisponible = models.IntegerField()
    cantidadAsientosOcupados = models.IntegerField()
    
