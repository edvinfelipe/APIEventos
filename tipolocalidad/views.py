from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TipoLocalidad
from .serializers import TipoLocalidadSerializers


# Create your views here.

class TipoLocalidadAPIView(APIView):

    def post(self, request):
        serializer = TipoLocalidadSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self, request):
        localidad = TipoLocalidad.objects.all()
        serializer = TipoLocalidadSerializers(localidad, many=True)
        return Response(serializer.data)