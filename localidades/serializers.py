from rest_framework import serializers
from .models import Localidad

class LocalidadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Localidad
        fields = '__all__'

class LocalidadModificacionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Localidad
        fields = ['costo','cantidadAsientos','cantidadAsientosDisponible','cantidadAsientosOcupados']