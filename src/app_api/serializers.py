from rest_framework.serializers import ModelSerializer
from autores.models import Autor, Frase

class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = ['nombre', 'nacionalidad', 'fecha_nacimiento', 'fecha_fallecimiento', 'activo', 'creado', 'modificado']
        # fields = '__all__'

class FraseSerializer(ModelSerializer):
    class Meta:
        model = Frase
        fields = '__all__'