from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Usuario

class UsuariosSerializers( serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class UsuariosModificacionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombre']
    
    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.save()
        return instance