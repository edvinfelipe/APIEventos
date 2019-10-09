from django.urls import path
from usuarios import views

urlpatterns = [
    path('api/usuarios/', views.UsuariosAPIView.as_view())
]