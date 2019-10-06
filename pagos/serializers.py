from rest_framework import serializers
from .models import Pago

class PagosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'