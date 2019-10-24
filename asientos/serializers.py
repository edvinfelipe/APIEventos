from rest_framework import serializers
from asientos.models import Asiento
from localidades.models import Localidad
from localidades.serializers import LocalidadSerializers

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

class ModificacionDisponibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asiento
        fields = ('disponible',)

class AsientosLocalidadesSerializer(serializers.ModelSerializer):
    #codigoEventos = LocalidadSerializers
    #codigoEventos = LocalidadSerializers(read_only=True)
    codigoEventos = LocalidadSerializers(many=True,read_only=True,source='codigoEvento_set')
    class Meta:
        model = Asiento
        fields = ('id','numeroAsiento','disponible','idLocalidad','codigoEventos')
        #model = Localidad
        #fields = ('id','codigoEventos',)