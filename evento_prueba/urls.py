from django.urls import path
from  .views import EventoAPIView

urlpatterns = [
    path('api/eventoprueba/', EventoAPIView.as_view())
]
