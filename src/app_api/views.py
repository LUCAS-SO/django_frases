from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from .serializers import AutorSerializer, FraseSerializer
from autores.models import Autor, Frase

# Create your views here.

# Solicitudes por APIView
#class AutorListCreateAPIView(ListCreateAPIView):
#    queryset = Autor.objects.all()
#    serializer_class = AutorSerializer


#class AutorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#    queryset = Autor.objects.all()
#    serializer_class = AutorSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)


class FraseViewSet(viewsets.ModelViewSet):
    queryset = Frase.objects.all()
    serializer_class = FraseSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,) 