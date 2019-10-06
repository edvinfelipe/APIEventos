from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UsuariosSerializers
from .models import Usuario
# Create your views here.
class UsuariosAPIView(APIView):

    def post(self, request):
        serializer = UsuariosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self, request):
        usuarios = Usuario.objects.all()
        serializer = UsuariosSerializers(usuarios, many= True)
        return Response(serializer.data)