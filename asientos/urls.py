from django.urls import path
from  asientos.views import AsientoLista, AsientoDetalles, getId, CodigoEventos

urlpatterns = [
    path('api/asientos/', AsientoLista.as_view()),
    path('api/asientos/codigoeventos/',CodigoEventos.as_view()),
    #path('api/asientos/getid/<int:pk>', getId.as_view())
    #path('api/asientos/', AsientoDetalles.as_view()),
]
