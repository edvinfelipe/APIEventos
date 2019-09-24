from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Localidad
from .serializers import LocalidadSerializers


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
        try:
            localidad = Localidad.objects.get(codigoEventos=codigo_evento, idTipoLocalidad=id_tipolocalidad)
        except Localidad.DoesNotExist:
            return Response({'Error': 'El evento o el tipo de localidad no concuerda'})

        serializer = LocalidadSerializers(localidad, many=False)
        return Response(serializer.data)