from django.urls import path 
from departamento import views

urlpatterns = [
    path('', views.Bienvenida.as_view()),
    path('api/departamento/', views.DepartamentAPIView.as_view())
]
