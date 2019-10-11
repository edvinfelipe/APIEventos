from django.urls import path
from  .views import EventoAPIView, EventoFilterFecha

urlpatterns = [
    path('api/eventos/', EventoAPIView.as_view()),
    path('api/eventos/fecha/', EventoFilterFecha.as_view())
]
