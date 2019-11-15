from django.db import models


# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=45)
    correo = models.CharField(max_length=45)
    rutaImagen = models.CharField(max_length=90, default = "")