from django.urls import path
from  asientos.views import AsientoLista, AsientoDetalles, getId,InnerJoin

urlpatterns = [
    path('api/asientos/', AsientoLista.as_view()),
    path('api/asientos/pruebas',InnerJoin.as_view()),
    #path('api/asientos/getid/<int:pk>', getId.as_view())
    #path('api/asientos/', AsientoDetalles.as_view()),
]
