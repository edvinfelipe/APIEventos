from rest_framework import serializers
from .models import ImagenUsuario

class ImagenUsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model  = ImagenUsuario
        fields = ['id','imagen','idUsuario']