from rest_framework import serializers
from asientos.models import Asiento

class AsientoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Asiento 
        fields = ('id','numeroAsiento','disponible','idLocalidad')
        #fields = '__all__'
        #fields = ('idLocalidad','idEventos','numeroAsiento','disponible')

class ModificacionAsientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asiento
        fields = ('id','numeroAsiento','idLocalidad')
