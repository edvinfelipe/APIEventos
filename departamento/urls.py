from django.urls import path 
from departamento import views

urlpatterns = [
    path('api/departamentos/', views.DepartamentAPIView.as_view())
]
