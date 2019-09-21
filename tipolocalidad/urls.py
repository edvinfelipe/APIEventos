from django.urls import path
from tipolocalidad import views

urlpatterns = [
    path('api/tipolocalidad/', views.TipoLocalidadAPIView.as_view())
]