from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import AutorSerializer, FraseSerializer
from autores.models import Autor, Frase

# Create your views here.

class AutorListAPIView(ListAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class AutorRetrieveAPIView(RetrieveAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class FraseListAPIView(ListAPIView):
    queryset = Frase.objects.all()
    serializer_class = FraseSerializer