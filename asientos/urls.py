from django.urls import path
from  asientos.views import EventoAPIView

urlpatterns = [
    path('api/asientos/', EventoAPIView.as_view())
]
