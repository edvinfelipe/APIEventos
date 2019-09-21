from rest_framework import serializers
from asientos.models import Asiento

class AsientoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Asiento 
        fields = ('numeroAsiento','disponible','idLocalidad','idEvento')