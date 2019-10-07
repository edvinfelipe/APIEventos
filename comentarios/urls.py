from django.urls import path
from .views import ComentarioAPIView
urlpatterns = [
    path('api/comentarios/',ComentarioAPIView.as_view())
]