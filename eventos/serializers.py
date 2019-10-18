from rest_framework import serializers
from .models import Evento


class EventoDepartamentSerializers( serializers.ModelSerializer ):
    idDepartamento = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='nombre'
     )
    class Meta:
        model = Evento
        fields  = ['codigo','titulo','descripcion','direccion','fecha','hora','disponible','rutaLugar','calificacionP','idDepartamento']

class EventoSerializers( serializers.ModelSerializer ):
    class Meta:
        model = Evento
        fields  = ['codigo','titulo','descripcion','direccion','fecha','hora','disponible','rutaLugar','calificacionP','idDepartamento']

class EventoSerializerModificacion( serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['titulo','descripcion','direccion','fecha','hora','disponible','rutaLugar','idDepartamento']
    
    # Actualiza un evento.
    def update(self, instance, validated_data):

        instance.titulo         = validated_data.get('titulo', instance.titulo)
        instance.descripcion    = validated_data.get('descripcion', instance.descripcion)
        instance.direccion      = validated_data.get('direccion', instance.direccion)
        instance.fecha          = validated_data.get('fecha', instance.fecha)
        instance.hora           = validated_data.get('hora', instance.hora)
        instance.disponible     = validated_data.get('disponible', instance.disponible)
        instance.rutaLugar      = validated_data.get('rutaLugar', instance.rutaLugar)
        instance.idDepartamento = validated_data.get('idDepartamento', instance.idDepartamento)
        instance.save()
        return instance