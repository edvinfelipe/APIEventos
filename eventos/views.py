from rest_framework.views import APIView
from rest_framework.response import Response
import random
from .models import Evento
from .serializers import EventoSerializers

# Create your views here.

def convertir_datos_json(data):
    json = {}
    codigo = data.get('codigo')
    imagenes = data.getlist('imagenes')
    
    
    if codigo is None:
        caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        codigo = "".join([random.choice(caracteres) for i in range(30)])
        
        # Verifica si el código no existe 
        while Evento.objects.filter(codigo=codigo).exists():
            codigo = "".join([random.choice(caracteres) for i in range(30)])
        
        json['codigo'] = codigo
    
    if imagenes is None:
        json['imagenes'] = []
    elif len(imagenes) is 1:
        json['imagenes'] = [{'imagen':imagenes[0]}]
    else:
        tempImagenes = []
        for imagen in imagenes:
            tempImagenes.append({'imagen':imagen})
        
        json['imagenes'] = tempImagenes

    json['id_departamento'] = data.get('id_departamento')
    json['titulo'] = data.get('titulo')
    json['descripcion'] = data.get('descripcion')
    json['direccion'] = data.get('direccion')
    json['fecha'] = data.get('fecha')
    json['disponible'] = data.get('disponible')
    json['rutaLugar'] = data.get('rutaLugar')
    return json
    

class EventoAPIView(APIView):

    def post(self, request):
         
        jsonevento = convertir_datos_json(request.data)

        serializer = EventoSerializers(data=jsonevento)
        print(jsonevento)
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
                return Response({'mensaje':'No existe el evento con el codigo enviado'})
            
            serializer = EventoSerializers(evento, many=False)
            return Response(serializer.data)
        




        



