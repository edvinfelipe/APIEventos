from django.db import models

# Create your models here.

class TipoLocalidad(models.Model):
    tipoLocalidad = models.CharField(max_length=45)