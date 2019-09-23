from rest_framework import serializers
from .models import Evento, Imagenes

class ImagenSerializers(serializers.ModelSerializer):
    class Meta:
        model = Imagenes
        fields = ['id','imagen']

class EventoSerializers( serializers.ModelSerializer ):
    imagenes = ImagenSerializers(many = True)
    class Meta:
        model = Evento
        fields  = ['codigo','titulo','descripcion','direccion','fecha','disponible','rutaLugar','calificacionP','id_departamento','imagenes']

    def create(self, validated_data):
        imagenes_evento = validated_data.pop('imagenes')
        evento          = Evento.objects.create(**validated_data)

        for imagen in imagenes_evento:
            Imagenes.objects.create(id_evento=evento, **imagen)
        return evento

class EventoSerializerModificacion( serializers.ModelSerializer):
    imagenes = ImagenSerializers(many=True)
    class Meta:
        model = Evento
        fields = ['titulo','descripcion','direccion','fecha','disponible','rutaLugar','id_departamento','imagenes']
    
    # Actualiza un evento.
    def update(self, instance, validated_data):
        
        images_agregar = validated_data.pop('imagenes')

        instance.titulo         = validated_data.get('titulo', instance.titulo)
        instance.descripcion    = validated_data.get('descripcion', instance.descripcion)
        instance.direccion      = validated_data.get('direccion', instance.direccion)
        instance.fecha          = validated_data.get('fecha', instance.fecha)
        instance.disponible     = validated_data.get('disponible', instance.disponible)
        instance.rutaLugar      = validated_data.get('rutaLugar', instance.rutaLugar)
        instance.id_departamento= validated_data.get('id_departamento', instance.id_departamento)
        instance.save()

        for image in images_agregar:
            Imagenes.objects.create(id_evento=instance, **image)
        
        return instance


