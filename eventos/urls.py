from django.urls import path
from  .views import EventoAPIView, EventoFilterFecha, List_evento

urlpatterns = [
    path('api/eventos/', EventoAPIView.as_view()),
    path('api/eventos/fecha/', EventoFilterFecha.as_view()),
    path('api/eventos/paginacion/', List_evento.as_view())
]
