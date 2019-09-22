from django.db import models
from django.db import models
from localidades.models import Localidad
from eventos.models import Evento
# Create your models here.

class Asiento( models.Model ):
    numeroAsiento = models.CharField(max_length=6)
    disponible = models.BooleanField()
    idLocalidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    idEvento = models.ForeignKey(Evento, on_delete=models.CASCADE)