from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from asientos.models import Asiento
from asientos.serializers import AsientoSerializers

class AsientoLista(APIView):
    """
    Lista todos los elementos de asiento, o crea un nuevo asiento
    """
    def get(self,request):
        #asiento2 = Asiento.objects.all()
        codigoLocalidad = request.GET.get('localidad')

        if codigoLocalidad is None:
            asiento = Asiento.objects.all()
            serializer = AsientoSerializers(asiento, many = True)
            return Response(serializer.data)
        else:
            try:
            
                asiento = Asiento.objects.filter(idLocalidad=codigoLocalidad)
            except asiento.DoesNotExist:
                return Response({'Error': 'El id de la localidad no existe (?)'})

            serializer = AsientoSerializers(asiento, many=True)
            return Response(serializer.data)

        #asiento = Asiento.objects.all()
        #serializer = AsientoSerializers(asiento, many = True)
        #return Response(serializer.data)

    def post(self,request):
        
        serializer = AsientoSerializers(data=request.data)
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
    def get(self,request,pk):
        asiento = self.get_object(pk)
        serializer = AsientoSerializers(asiento)
        return Response (serializer.data)
    def put(self,request,pk):
        asiento = self.get_object(pk)
        serializer = AsientoSerializers(asiento,data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        asiento = self.get_object(pk)
        asiento.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class getId(APIView):
    def get(self,request,pk):
        try:
            id_asiento = pk
            asiento = Asiento.objects.get(id=id_asiento)
        except asiento.DoesNotExist:
            return Response({'Error': 'El id del asiento no existe (?)'})

        serializer = AsientoSerializers(asiento, many=False)
        return Response(serializer.data)