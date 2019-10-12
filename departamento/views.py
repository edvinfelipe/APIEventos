from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Departamento
from .serializers import DepartamentSerializers
from django.http import HttpResponse

# Create your views here.

class DepartamentAPIView(APIView):

    def post(self, request):
        serializer = DepartamentSerializers(data=request.data)
        if serializer.is_valid():          
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def get(self, request):
        departamentos = Departamento.objects.all()
        serializer = DepartamentSerializers(departamentos, many= True)
        return Response(serializer.data)



class Bienvenida(APIView):

    def get(self, request):
        return HttpResponse('<h1>Bienvenido</h1>')

