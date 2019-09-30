from django.db import models

# Create your models here.
class Pago(models.Model):
    tipoPaogo = models.CharField(max_length=45)