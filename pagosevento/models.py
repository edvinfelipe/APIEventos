from django.db import models
from pagos.models import Pago

class PagosEvento(models.Model):
    codigoEventos = models.CharField(max_length=45, null=True)
    idPago = models.ForeignKey(Pago, null=True, on_delete=models.CASCADE)