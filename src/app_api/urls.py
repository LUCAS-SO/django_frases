from django.urls import path
from .views import (
    AutorListCreateAPIView,
    AutorRetrieveUpdateDestroyAPIView,
    FraseListCreateAPIView,
    FraseRetrieveUpdateDestroyAPIView,
)

app_name = 'app_api'

urlpatterns = [
    path('', AutorListCreateAPIView.as_view(), name='autores_lc_api'),
    path('<int:pk>/', AutorRetrieveUpdateDestroyAPIView.as_view(), name='autores_rud_api'),
    path('frases/', FraseListCreateAPIView.as_view(), name='frases_lc_api'),
    path('frases/<int:pk>/', FraseRetrieveUpdateDestroyAPIView.as_view(), name='frases_rud_api'),
]
