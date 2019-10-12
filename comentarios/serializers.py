from rest_framework import serializers
from .models import Comentario

class ComentarioUserSerializers(serializers.ModelSerializer):
    idUsuario = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='nombre'
     )

    class Meta:
        model = Comentario
        fields = ['id','descripcion','calificacion','codigoEvento','idUsuario']

class ComentarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id','descripcion','calificacion','codigoEvento','idUsuario']

class ComentarioModificacionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['descripcion','calificacion']
    
    def update(self, instance, validated_data):
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.calificacion = validated_data.get('calificacion', instance.calificacion)
        instance.save()
        return instance