from django.urls import path
from  .views import EventoAPIView

urlpatterns = [
    path('api/eventos/', EventoAPIView.as_view())
]
