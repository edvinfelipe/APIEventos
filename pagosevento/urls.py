from django.urls import path
from pagosevento import views

urlpatterns = [
    path('api/pagosevento/', views.PagosEventoAPIView.as_view())
]