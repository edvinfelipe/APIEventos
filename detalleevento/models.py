from django.db import models
from django.db import models
from asientos.models import Asiento
from usuarios.models import Usuario 
from pagos.models import Pago

class DetalleEvento( models.Model):
    codigoEvento = models.CharField(max_length=45)
    pago = models.DecimalField(max_digits=15, decimal_places= 4)
    reserva = models.BooleanField()
    idUsuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    idAsiento = models.ForeignKey(Asiento, on_delete=models.CASCADE)
    idTipoPago = models.ForeignKey(Pago, on_delete=models.CASCADE)

