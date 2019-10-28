from django.db import models
from usuarios.models import Usuario

class ImagenUsuario(models.Model):
    imagen = models.ImageField()
    eliminado = models.BooleanField(default=False)
    idUsuario = models.ForeignKey(Usuario ,on_delete=models.CASCADE)

    def deleted(self):
        self.eliminado = True
        self.save()