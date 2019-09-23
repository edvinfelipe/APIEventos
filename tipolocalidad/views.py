from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TipoLocalidad
from .serializers import TipoLocalidadSerializers
import json



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
