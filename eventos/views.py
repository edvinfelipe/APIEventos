from rest_framework.views import APIView
from rest_framework.response import Response
import random
from .models import Evento
from .serializers import EventoSerializers, EventoSerializerModificacion
from imagenes import views

def convertir_datos_json(data):
    json = {}
    codigo = data.get('codigo') 
    
    if codigo is None:
        caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        codigo = "".join([random.choice(caracteres) for i in range(30)])
        
        # Verifica si el código no existe 
        while Evento.objects.filter(codigo=codigo).exists():
            codigo = "".join([random.choice(caracteres) for i in range(30)])
        
        json['codigo'] = codigo
    

    json['titulo']      =    data.get('titulo')
    json['descripcion'] =    data.get('descripcion')
    json['direccion']   =    data.get('direccion')
    json['fecha']       =    data.get('fecha')
    json['hora']        =    data.get('hora') 
    json['disponible']  =    data.get('disponible')
    json['rutaLugar']   =    data.get('rutaLugar')
    json['idDepartamento'] = data.get('idDepartamento')

    return json

class EventoAPIView(APIView):

    def post(self, request):
         
        jsonevento = convertir_datos_json(request.data)

        serializer = EventoSerializers(data=jsonevento)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def get(self, request):
        codigo_evento = request.GET.get('codigo')

        if codigo_evento is None:
            try:
                eventos = Evento.objects.filter(eliminado=False)
            except Evento.DoesNotExist:
                return Response({})
            
            serializer = EventoSerializers(eventos, many = True) 
            return Response(serializer.data)
        
        else:
            try:
                evento = Evento.objects.get(codigo=codigo_evento, eliminado=False)
            except Evento.DoesNotExist:
                return Response({'Error':'No existe el evento con el codigo enviado'})
            
            serializer = EventoSerializers(evento, many=False)
            return Response(serializer.data)
    
    def put(self,request):
        codigo_evento = request.GET.get('codigo')

        if codigo_evento is None:
            return Response({'Error':'No existe el evento'})
        
        try:
            evento = Evento.objects.get(codigo=codigo_evento, eliminado=False)
        except Evento.DoesNotExist:
            return Response({'Error':'No existe el evento'})

        serializer = EventoSerializerModificacion(evento, data= request.data)

        if serializer.is_valid():            
            serializer.save()
            
            return Response({'mensaje':'Evento modificado con éxito'})
        return Response({'Error':'Fallo en la modificación'})

    def delete(self, request):
        codigo_evento = request.GET.get('codigo')

        if codigo_evento is None:
            return Response({'Error':'No existe el evento'})
        
        try:
            evento = Evento.objects.get(codigo=codigo_evento)
            evento.deleted()
            views.eliminar_imagenes_evento(codigo_evento)
            return Response({'mensaje':'Evento eliminado con éxito'})
        except Evento.DoesNotExist:
            return Response({'Error':'No existe el evento'})
