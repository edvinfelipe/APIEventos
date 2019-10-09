from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from detalleevento.models import DetalleEvento
from detalleevento.serializers import DetalleEventoSerializers


class DetalleEventoLista(APIView):
    """
    Lista todos los elementos de asiento, o crea un nuevo asiento
    """
    ##global codigoAsiento
    def get(self,request):
        detalleevento = DetalleEvento.objects.all()
        serializer = DetalleEventoSerializers(detalleevento,many=True)
        return Response(serializer.data)

    """def post(self,request):
        serializer = DetalleEventoSerializers(data=request.data)
        if(serializer.is_valid):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)"""
