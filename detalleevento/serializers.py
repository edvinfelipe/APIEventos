from rest_framework import serializers
from detalleevento.models import DetalleEvento

class DetalleEventoSerializers(serializers.ModelSerializer):
    class Meta:
        model = DetalleEvento 
        fields = '__all__'
        #fields = ('id','codigoEvento','pago','reserva','idUsuario','idAsiento')
