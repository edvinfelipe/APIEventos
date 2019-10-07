from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Localidad
from .serializers import LocalidadSerializers
from tipolocalidad.models import TipoLocalidad
from tipolocalidad.serializers import TipoLocalidadSerializers
from .serializers import LocalidadModificacionSerializers

class LocalidadAPIView(APIView):

    def post(self, request):

        serializer = LocalidadSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self, request):
        codigo_evento = request.GET.get('codigoEventos')
        id_tipolocalidad = request.GET.get('idTipoLocalidad')
        if (codigo_evento is None) and (id_tipolocalidad is None):
            try:
                localidad = Localidad.objects.all()
            except Localidad.DoesNotExist:
                return Response()

            serializer = LocalidadSerializers(localidad, many=True)
            return Response(serializer.data)

        elif(codigo_evento is not None) and (id_tipolocalidad is None):
            try:
                localidad = Localidad.objects.filter(codigoEventos=codigo_evento)
                serializerlocalidad = LocalidadSerializers(localidad, many=True)
                tipolocalidad = []
                for local in serializerlocalidad.data:
                    tipolocal = TipoLocalidad.objects.filter(pk=local.get('idTipoLocalidad'))
                    tipolocalidad.extend(tipolocal)
            except TipoLocalidad.DoesNotExist:
                return Response({"Error": 'Código de evento incorrecto'})

            serializer = TipoLocalidadSerializers(tipolocalidad, many=True)
            return Response(serializer.data)

        elif (codigo_evento is not None) and (id_tipolocalidad is not None):
            try:
                localidad = Localidad.objects.get(codigoEventos=codigo_evento, idTipoLocalidad=id_tipolocalidad)
            except Localidad.DoesNotExist:
                return Response({'Error': 'El evento o el tipo de localidad no coinciden'})

            serializer = LocalidadSerializers(localidad, many=False)
            return Response(serializer.data)

    def put(self, request):
        id_localidad = request.GET.get('id')
        if(id_localidad is None):
            return Response()
        else:
            try:
                localidad = Localidad.objects.get(id=id_localidad)
            except Localidad.DoesNotExist:
                return Response({'Error':'No existe la localidad'})

            serializer = LocalidadModificacionSerializers(localidad, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({'Mensaje': 'Localidad modificada con éxito'})
            return Response({'Error': 'Fallo en la modificación'})