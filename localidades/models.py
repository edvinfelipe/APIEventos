from django.db import models
from tipolocalidad.models import TipoLocalidad
from eventos.models import Evento

class Localidad( models.Model):
    costo = models.DecimalField(max_digits=15, decimal_places= 4)
    cantidadAsientos = models.IntegerField()
    cantidadAsientosDisponible = models.IntegerField(blank=True)
    cantidadAsientosOcupados = models.IntegerField(blank=True)
    idEventos = models.ForeignKey(Evento, null=True, on_delete=models.CASCADE)
    idTipoLocalidad = models.ForeignKey(TipoLocalidad, null=True, on_delete=models.CASCADE)
