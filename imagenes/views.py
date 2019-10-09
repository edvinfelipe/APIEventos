from rest_framework.views import APIView
from .serializers import ImageneSerializers
from eventos.models import Evento
from .models import Imagenes
from rest_framework.response import Response
# Create your views here.
class ImagenesAPIView( APIView):

    def post(self, request):

        codigo_evento = request.GET.get('codigo')

        if Evento.objects.filter(codigo=codigo_evento, eliminado=False).exists():
            
            serializer = ImageneSerializers(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        return Response({'Error':'No existe el evento, verifica el código'})
    
    def get(self, request):
        codigo_evento = request.GET.get('codigo')
        try:
            imagenes = Imagenes.objects.filter(codigoEvento=codigo_evento,eliminado=False)
            serializer = ImageneSerializers(imagenes, many = True)
            return Response(serializer.data)
        except:
            return Response({'Error':'No existe imagenes de este evento'})
    
    def delete(self, request):
        codigo_evento = request.GET.get('codigo')

        if Evento.objects.filter(codigo=codigo_evento, eliminado=False).exists():

            try:    
                id_imagenes = request.data.get('id')
                for id in id_imagenes:
                    imagen = Imagenes.objects.get(pk=id,eliminado=False)
                    imagen.deleted()
                    
                return Response({'mensaje':'La imagen se eliminó con éxito'})
            except:
                return Response({'Error':'Hubo error en la eliminación de una imagen'})
                
        return Response({'Error':'No existe el evento'})


# Elimina todas las imagénes de un evento si este es eliminado
def eliminar_imagenes_evento(codigo_evento):
        imagenes = Imagenes.objects.filter(codigoEvento=codigo_evento,eliminado=False)
        serializer = ImageneSerializers(imagenes, many = True)

        for imagen in serializer.data:
            imagen = Imagenes.objects.get(pk=imagen.get('id'))
            imagen.deleted()
       
  
