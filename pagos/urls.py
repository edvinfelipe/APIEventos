from django.urls import path
from pagos import views

urlpatterns = [
    path('api/pagos/', views.PagosAPIView.as_view())
]