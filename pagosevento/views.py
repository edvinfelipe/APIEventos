from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PagosEventoSerializers
from .models import PagosEvento

class PagosEventoAPIView(APIView):
    def post(self, request):
        serializer = PagosEventoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self, request):
        codigo_evento = request.GET.get('codigoEventos')
        if (codigo_evento is None):
            try:
                pagosEvento = PagosEvento.objects.all()
            except PagosEvento.DoesNotExist:
                return Response()

            serializer = PagosEventoSerializers(pagosEvento, many=True)
            return Response(serializer.data)

        elif(codigo_evento is not None):
            try:
                pagosEvento = PagosEvento.objects.filter(codigoEventos=codigo_evento)
            except PagosEvento.DoesNotExist:
                return Response({'Error': 'El evento no coincide'})

            serializer = PagosEventoSerializers(pagosEvento, many=True)
            return Response(serializer.data)