from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from asientos.models import Asiento
from asientos.serializers import AsientoSerializers

class AsientoLista(APIView):
    """
    List all asiento, or create new asiento
    """
    def get(self,request,format=None):
        asiento = Asiento.objects.all()
        serializer = AsientoSerializers(asiento)
        return Response(serializer.data)
    def post(self,request,format=None):
        serializer = AsientoSerializers(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class AsientoDetalles(APIView):
    '''
    Get, update, or delete a specific asiento 
    '''

    def get_object(self,pk):
        try:
            return Asiento.objects.get(pk=pk)
        except Asiento.DoesNotExist:
            raise Http404
    def get(self,request,pk,format=None):
        asiento = self.get_object(pk)
        serializer = AsientoSerializers(asiento)
        return Response (serializer.data)
    def put(self,request,pk,format=None):
        asiento = self.get_object(pk)
        serializer = AsientoSerializers(asiento,data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        asiento = self.get_object(pk)
        asiento.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)