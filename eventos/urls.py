from django.urls import path
from  .views import EventoAPIView

urlpatterns = [
    path('api/evento/', EventoAPIView.as_view())
]
