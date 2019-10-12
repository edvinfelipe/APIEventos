from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TipoLocalidad
from .serializers import TipoLocalidadSerializers
from .serializers import TipoLocalidadModificacionSerializers



class TipoLocalidadAPIView(APIView):

    def post(self, request):
        serializer = TipoLocalidadSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


    def get(self, request):
         try:
             localidad = TipoLocalidad.objects.all()
         except TipoLocalidad.DoesNotExist:
             return Response({})
         serializer = TipoLocalidadSerializers(localidad, many=True)
         return Response(serializer.data)

    def put(self, request):
        id_tipoLocalidad = request.GET.get('id')
        if (id_tipoLocalidad is None):
            return Response()
        elif (id_tipoLocalidad is not None):
            try:
                tipoLocalidad = TipoLocalidad.objects.get(id=id_tipoLocalidad)
            except TipoLocalidad.DoesNotExist:
                return Response({'Error': 'No existe la localidad'})

            serializer = TipoLocalidadModificacionSerializers(tipoLocalidad, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({'Mensaje': 'Localidad modificada con éxito'})
            return Response({'Error': 'Falló la modificación'})
