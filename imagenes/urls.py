from django.urls import path
from .views import ImagenesAPIView

urlpatterns = [
    path('api/imagenes/', ImagenesAPIView.as_view())
]
