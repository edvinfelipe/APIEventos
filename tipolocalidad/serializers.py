from rest_framework import serializers
from .models import TipoLocalidad

class TipoLocalidadSerializers(serializers.ModelSerializer):
    class Meta:
        model = TipoLocalidad
        fields = '__all__'
class TipoLocalidadModificacionSerializers(serializers.ModelSerializer):
    class Meta:
        model = TipoLocalidad
        fields = ['tipoLocalidad']