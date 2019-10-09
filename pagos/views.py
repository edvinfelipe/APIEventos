from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PagosSerializers
from .models import Pago

# Create your views here.
class PagosAPIView(APIView):

    def post(self, request):
        serializer = PagosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self, request):
        pagos = Pago.objects.all()
        serializer = PagosSerializers(pagos, many= True)
        return Response(serializer.data)