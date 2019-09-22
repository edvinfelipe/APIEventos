from django.urls import path
from  asientos.views import AsientoLista, AsientoDetalles

urlpatterns = [
    path('api/asientos/', AsientoLista.as_view()),
    #path('api/asientos/', AsientoDetalles.as_view()),
]
