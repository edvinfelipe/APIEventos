from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Usuario

class UsuariosSerializers( serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        extra_kwargs = {'contrasena': {'write_only': True}}

    def create(self, validated_data):
        usuario = Usuario(
            nombre=validated_data['nombre'],
            correo=validated_data['correo'],
            contrasena = make_password(validated_data['contrasena'])
        )
        return usuario