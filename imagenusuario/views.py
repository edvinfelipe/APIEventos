from rest_framework.views import APIView
from .serializers import ImagenUsuarioSerializers
from usuarios.models import Usuario
from .models import ImagenUsuario
from rest_framework.response import Response

class ImagenUsuarioAPIView(APIView):

    def post(self, request):

        idUsuario = request.data.get('idUsuario')

        print("Este es el usuario No: ", request.data.get('idUsuario'))
        if Usuario.objects.filter(id=idUsuario).exists():

            serializer = ImagenUsuarioSerializers(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        return Response({'Error': 'No existe el usuario'})

    def get(self, request):
        idUsuario = request.GET.get('idUsuario')
        try:
            imagenes = ImagenUsuario.objects.filter(idUsuario=idUsuario, eliminado=False)
            serializer = ImagenUsuarioSerializers(imagenes, many=True)
            return Response(serializer.data)
        except:
            return Response({'Error': 'No hay imágenes existentes de este usuario'})

    def delete(self, request):
        idUsuario = request.GET.get('idUsuario')

        if Usuario.objects.filter(idUsuario=idUsuario).exists():

            try:
                id_imagenes = request.data.get('id')
                for id in id_imagenes:
                    imagen = ImagenUsuario.objects.get(pk=id, eliminado=False)
                    imagen.deleted()

                return Response({'mensaje': 'La imagen se eliminó con éxito'})
            except:
                return Response({'Error': 'Hubo error en la eliminación de una imagen'})

        return Response({'Error': 'No existe el usuario'})


# Elimina todas las imagénes de un evento si este es eliminado
def eliminar_imagenes_evento(idUsuario):
    imagenes = ImagenUsuario.objects.filter(idUsuario=idUsuario, eliminado=False)
    serializer = ImagenUsuarioSerializers(imagenes, many=True)

    for imagen in serializer.data:
        imagen = ImagenUsuario.objects.get(pk=imagen.get('id'))
        imagen.deleted()