from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from asientos.models import *
from asientos.serializers import AsientoSerializers, AsientosLocalidadesSerializer, ModificacionDisponibleSerializer, ModificacionAsientoSerializer
from asientos.pagination import ViewPagination1

class AsientoLista(APIView):
    """
    Lista todos los elementos de asiento, o crea un nuevo asiento
    """
    ##global codigoAsiento
    def get(self,request):
        codigoLocalidad = request.GET.get('idLocalidad')
        codigoAsiento = request.GET.get('idAsiento')
        codigoEvento = request.GET.get('codigoEvento')

        if (codigoLocalidad is None) and (codigoAsiento is None):
            asiento = Asiento.objects.all()
            serializer = AsientoSerializers(asiento, many = True)
            return Response(serializer.data)

        elif((codigoLocalidad != '') and (codigoAsiento is None)):
            try:
                asiento = Asiento.objects.filter(idLocalidad=codigoLocalidad)
                pagination = ViewPagination1()
                result_page = pagination.paginate_queryset(asiento,request)
            except asiento.DoesNotExist:
                return Response({'Error': 'El id de la localidad no existe (?)'})
            #serializer = AsientoSerializers(asiento, many=True)
            serializer = AsientoSerializers(result_page, many=True)
            #return Response(serializer.data)
            return pagination.get_paginated_response(serializer.data)

        elif((codigoLocalidad is None) and (codigoAsiento != '')):    
            try:
                asiento = Asiento.objects.get(id = codigoAsiento)
                if asiento.disponible == False:
                    serializer = ModificacionDisponibleSerializer(asiento,many=False)
                    return Response(serializer.data)
            except Asiento.DoesNotExist:
                return Response({'Error': 'El id de la localidad no existe (?)'})
                
            serializer = AsientoSerializers(asiento, many=False)
            return Response(serializer.data)
    
        elif((codigoEvento != '')and(codigoLocalidad != '')):
            try:   
                asiento = AsientoconCodigoEvento.objects.filter(idLocalidad=codigoLocalidad,codigoAsiento=codigoAsiento)
            except asiento.DoesNotExist:
                return Response({'Error':'No se encontró ningún criterio de la búsqueda'})
            serializer = LocalidadCodigoEventoSerializer(asiento,many=True)
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

    def put(self,request):
        codigoAsiento = request.GET.get('idAsiento')
        try:
            asiento = Asiento.objects.get(id=codigoAsiento)
        except asiento.DoesNotExist:
            return Response({'Error': 'El id del asiento no existe (?)'})
            #asiento = self.get_object(pk)
        if codigoAsiento is None:
            return Response({'Error':'No existe el asiento'})
        else:
            if asiento.disponible == False:
                return Response({'Error' : 'Este asiento no se encuentra disponible'})
            else:
                asiento.disponible = False
                serializer = ModificacionAsientoSerializer(asiento,data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                

class CodigoEventos(APIView):
    #queryset = Asiento.objects.filter(idLocalidad=1).select_related('idLocalidad')#.prefetch_related(Prefetch('id','codigoEventos')
    #print(str(queryset.query))
    #serializer_class = AsientoSerializers
    def get(self,request):
        codigoLocalidad = request.GET.get('idLocalidad')
        if (codigoLocalidad is None):
            return Response({'Error': 'No se realizo ninguna búsqueda'})
        else:
            asiento = Asiento.objects.filter(idLocalidad=codigoLocalidad).select_related('idLocalidad')
            #print (str(asiento.query))
            serializer = AsientosLocalidadesSerializer(asiento, many = True)
            return Response(serializer.data)










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

    def delete(self,request,pk):
        asiento = self.get_object(pk)
        asiento.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class getId(APIView):
    def get(self,request,pk):
        try:
            id_asiento = pk
            asiento = Asiento.objects.get(idAsiento=id_asiento)
        except asiento.DoesNotExist:
            return Response({'Error': 'El id del asiento no existe (?)'})

        serializer = AsientoSerializers(asiento, many=False)
        return Response(serializer.data)