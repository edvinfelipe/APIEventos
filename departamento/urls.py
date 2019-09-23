from django.urls import path 
from departamento import views

urlpatterns = [
    path('api/departamento/', views.DepartamentAPIView.as_view())
]
