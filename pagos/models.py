from django.db import models

# Create your models here.
class Pago(models.Model):
    tipoPago = models.CharField(max_length=45)