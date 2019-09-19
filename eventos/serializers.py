from rest_framework import serializers
from .models import Evento, Imagenes

class ImagenSerializers(serializers.ModelSerializer):
    class Meta:
        model = Imagenes
        fields = ['imagen']

class EventoSerializers( serializers.ModelSerializer ):
    imagenes = ImagenSerializers(many = True)
    class Meta:
        model = Evento
        fields  = ['codigo','titulo','descripcion','direccion','fecha','disponible','rutaLugar','calificacionP','id_departamento','imagenes']

    def create(self, validated_data):
        imagenes_evento = validated_data.pop('imagenes')
        evento = Evento.objects.create(**validated_data)

        for imagen in imagenes_evento:
            Imagenes.objects.create(id_evento=evento, **imagen)
        return evento
