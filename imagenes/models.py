from django.db import models
from eventos.models import Evento

# Create your models here.
class Imagenes(models.Model):
    imagen          = models.ImageField()
    eliminado       = models.BooleanField(default=False)
    codigoEvento    = models.CharField(max_length=50)

    def deleted(self):
        self.eliminado = True
        self.save()