from django.urls import path 
from departamento import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.Bienvenida.as_view()),
    path('api/departamento/', views.DepartamentAPIView.as_view())
=======
    path('api/departamentos/', views.DepartamentAPIView.as_view())
>>>>>>> felipe
]
