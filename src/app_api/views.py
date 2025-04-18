from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import AutorSerializer, FraseSerializer
from autores.models import Autor, Frase

# Create your views here.

class AutorListCreateAPIView(ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class AutorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class FraseListCreateAPIView(ListCreateAPIView):
    queryset = Frase.objects.all()
    serializer_class = FraseSerializer


class FraseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Frase.objects.all()
    serializer_class = FraseSerializer