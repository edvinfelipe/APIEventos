from rest_framework.views import APIView
from rest_framework.response import Response
import random
from .models import Evento, Imagenes
from .serializers import EventoSerializers, EventoSerializerModificacion

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

    json['titulo']      =    data.get('titulo')
    json['descripcion'] =    data.get('descripcion')
    json['direccion']   =    data.get('direccion')
    json['fecha']       =    data.get('fecha')
    json['disponible']  =    data.get('disponible')
    json['rutaLugar']   =     data.get('rutaLugar')
    json['id_departamento'] = data.get('id_departamento')

    return json

def convertir_datos_modificar_json(data, json):
    
    imagenes_borrar = data.getlist('imagenes_borrar')
    
    if imagenes_borrar is None:
        json['imagenes_borrar'] = []
    elif len(imagenes_borrar) is 1:
        json['imagenes_borrar'] = [{'pk':imagenes_borrar[0]}]
    else:
        tempImBorrar = []
        for id in imagenes_borrar:
            tempImBorrar.append({'pk':id})
        json['imagenes_borrar'] = tempImBorrar
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
                return Response({'Error':'No existe el evento con el codigo enviado'})
            
            serializer = EventoSerializers(evento, many=False)
            return Response(serializer.data)
    
    def put(self,request):
        codigo_evento = request.GET.get('codigo')

        if codigo_evento is None:
            return Response({'Error':'No existe el evento'})
        
        try:
            evento = Evento.objects.get(codigo=codigo_evento)
        except Evento.DoesNotExist:
            return Response({'Error':'No existe el evento'})

        jsonevento = convertir_datos_json(request.data)                         # Retorno solo el json del evento.                    
        tempjson = convertir_datos_modificar_json(request.data,jsonevento)      # Retorna el json con imagenes a agregar y borrar
        list_img_borrar = tempjson.pop('imagenes_borrar')
        serializer = EventoSerializerModificacion(evento, data= jsonevento)

        if serializer.is_valid():

            for id in list_img_borrar:
                try:
                    Imagenes.objects.filter(pk=id['pk']).delete()
                except Imagenes.DoesNotExist:
                    return Response({'Error': 'Hubo error al eliminar la imagene, verifica el id'})
            
            serializer.save()
            
            return Response({'mensaje':'Evento modificado con éxito'})
        return Response({'Error':'Fallo en la modificación'})
