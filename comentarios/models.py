from django.db import models
from usuarios.models import Usuario

# Create your models here.
class Comentario(models.Model):
    descripcion     = models.TextField()
    calificacion    = models.IntegerField(default=0)
    fecha           = models.DateField(auto_now_add=True)
    codigoEvento    = models.CharField(max_length=50)
    idUsuario       = models.ForeignKey(Usuario,on_delete=models.CASCADE, related_name='usuario')