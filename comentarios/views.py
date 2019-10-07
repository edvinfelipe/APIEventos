from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Comentario
from eventos.models import Evento
from .serializers import ComentarioSerializers, ComentarioModificacionSerializers, ComentarioUserSerializers

# Create your views here.
class ComentarioAPIView(APIView):

    def post(self, request):
        codigo_evento = request.GET.get('codigo')
        try:
            evento = Evento.objects.get(codigo=codigo_evento, eliminado=False) 
        except Evento.DoesNotExist:
            return Response({'Error': 'No existe el evento'})      
            
        serializer = ComentarioSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            evento.updated(int(serializer.data.get('calificacion')))
            coment1 = Comentario.objects.get(pk=serializer.data.get('id'))
            serializer1 = ComentarioUserSerializers(instance=coment1)
            return Response(serializer1.data)
        return Response(serializer.errors)

    def get(self, request):
        codigo_evento = request.GET.get('pk')

        if codigo_evento is None:
            return Response({'Error':'Parámetro incorrecto'})

        try:
            comentarios = Comentario.objects.filter(codigoEvento=codigo_evento)
            serializer = ComentarioUserSerializers(comentarios, many=True)
            return Response(serializer.data)
        except:
            return Response({'Error':'No hay comentarios al evento'})
            #return Response({'Error':'No existe comentario de este evento'})  
    
    def put(self, request):
        pk = request.GET.get('pk')

        if pk is None:
            return Response({'Error':'Parámetro incorrecto'})
        try:
            comentario = Comentario.objects.get(pk=pk)
            serializer = ComentarioModificacionSerializers(comentario, data=request.data)
            if serializer.is_valid():
                serializer.save()

                evento = Evento.objects.get(codigo=comentario.codigoEvento, eliminado=False)
                evento.updated(int(serializer.data.get('calificacion')))

                return Response(serializer.data)
            return Response(serializer.errors)
        except:
            return Response({'Error':'Hubo error en la modificación del comentario'})
    
    def delete(self, request):
        pk = request.GET.get('pk')

        if pk is None:
            return Response({'Error':'Parámetro incorrecto'})

        try:
            comentario = Comentario.objects.get(pk=pk)
            comentario.delete()
            return Response({'mensaje':'El comentario se eliminó con éxito'})
        except:
            return Response({'Error':'Fallo en la eliminación'})

def eliminar_comentarios_evento(codigo_evento):
        comentarios = Comentario.objects.filter(codigoEvento=codigo_evento)
        serializer = ComentarioSerializers(comentarios, many = True)

        for coment in serializer.data:
            comentario = Comentario.objects.get(pk=coment.get('id'))
            comentario.delete()