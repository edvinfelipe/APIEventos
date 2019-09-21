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
        localidad = Localidad.objects.all()
        serializer = LocalidadSerializers(localidad, many=True)
        return Response(serializer.data)