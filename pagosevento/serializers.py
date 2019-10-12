from rest_framework import serializers
from .models import PagosEvento

class PagosEventoSerializers(serializers.ModelSerializer):
    class Meta:
        model = PagosEvento
        fields = '__all__'