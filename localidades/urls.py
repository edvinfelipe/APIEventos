from django.urls import path
from localidades import views

urlpatterns = [
    path('api/localidad/', views.LocalidadAPIView.as_view())
]