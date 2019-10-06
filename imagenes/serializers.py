from rest_framework import serializers
from .models import Imagenes

class ImageneSerializers( serializers.ModelSerializer):
    class Meta:
        model  = Imagenes
        fields = ['id','imagen','codigoEvento']