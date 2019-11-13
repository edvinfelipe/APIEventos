from django.db import models
from django.db import models
from localidades.models import Localidad
from eventos.models import Evento
#from detalleevento.models import DetalleEvento
# Create your models here.

class Asiento( models.Model ):
    numeroAsiento = models.CharField(max_length=6)
    disponible = models.BooleanField()
    idLocalidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    #codigoEventos = models.ForeignKey(Localidad,related_name='codigoEventos',on_delete=models.SET_NULL)
    #idEvento = models.ForeignKey(Evento, on_delete=models.CASCADE)

