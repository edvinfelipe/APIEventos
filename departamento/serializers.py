from rest_framework import serializers
from .models import Departamento

class DepartamentSerializers( serializers.ModelSerializer):
    class Meta:
        model = Departamento
        #fields = ('id','nombre',)
        fields = '__all__'