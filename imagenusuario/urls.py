from django.urls import path
from .views import ImagenUsuarioAPIView

urlpatterns = [
    path('api/imagenusuario/', ImagenUsuarioAPIView.as_view())
]