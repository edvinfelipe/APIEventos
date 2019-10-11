from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from detalleevento.models import DetalleEvento
from detalleevento.serializers import DetalleEventoSerializers, ModificacionDetalleEventoSerializer


class DetalleEventoLista(APIView):
    """
    Lista todos los elementos de detalleevento, o bien ya se por filtros los cuales pueden ser por id, codigoEvento y idUsuario
    """
    ##global codigoAsiento
    def get(self,request):
        idUsuario = request.GET.get("idUsuario")
        idDetalle = request.GET.get("idDetalleEvento")
        codigoEvento = request.GET.get("codigoEvento")
        if((idUsuario is None) and (idDetalle is None) and(codigoEvento is None)):
            detalleevento = DetalleEvento.objects.all()
            serializer = DetalleEventoSerializers(detalleevento,many=True)
            return Response(serializer.data)
        elif((idUsuario != "")and (idDetalle is None) and(codigoEvento is None)):
            try:
                detalleevento = DetalleEvento.objects.filter(idUsuario=idUsuario)
            except detalleevento.DoesNotExist:
                return Response({'Error': 'El id del usuario de la tabla detalleevento no existe (?)'})
            serializer = DetalleEventoSerializers(detalleevento,many=True)
            return Response(serializer.data)
        elif((idUsuario is None) and (idDetalle != "") and(codigoEvento is None)):
            try:
                detalleevento = DetalleEvento.objects.filter(id=idDetalle)
            except detalleevento.DoesNotExist:
                return Response({'Error': 'El id del detalleevento no existe (?)'})
            serializer = DetalleEventoSerializers(detalleevento,many=True)
            return Response(serializer.data)
        elif((idUsuario is None) and (idDetalle is None) and(codigoEvento != "")):
            try:
                detalleevento = DetalleEvento.objects.filter(codigoEvento=codigoEvento)
            except detalleevento.DoesNotExist:
                return Response({'Error': 'El id del codigo de evento de la tabla detalleevento no existe (?)'})
            serializer = DetalleEventoSerializers(detalleevento,many=True)
            return Response(serializer.data)

            


    def post(self,request):
        serializer = DetalleEventoSerializers(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request):
        idDetalle = request.GET.get("idDetalleEvento")
        if(idDetalle is None):
            return Response({'Error':'No existe el asiento'})
        else:
            try:
                detalleevento=DetalleEvento.objects.get(id=idDetalle)
            except detalleevento.DoesNotExist:
                return Response({'Error': 'El id del detalleevento no existe (?)'})
            serializer = ModificacionDetalleEventoSerializer(detalleevento,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
