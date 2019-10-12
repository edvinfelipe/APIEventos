from django.urls import path
from  detalleevento.views import DetalleEventoLista

urlpatterns = [
    path('api/detalleevento/', DetalleEventoLista.as_view()),
]
