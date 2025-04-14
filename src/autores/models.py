from django.db import models

# Create your models here.

class Autor(models.Model):
    NACIONALIDADES = [
        ('AR', 'Argentina'),
        ('BR', 'Brasil'),
        ('CL', 'Chile'),
        ('CO', 'Colombia'),
        ('ES', 'España'),
        ('MX', 'México'),
        ('US', 'Estados Unidos'),
        ('DE', 'Alemania'),
        ('IN', 'India'),
    ]

    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=2, choices=NACIONALIDADES)
    fecha_nacimiento = models.DateField()
    fecha_fallecimiento = models.DateField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nombre} {self.nacionalidad} {self.fecha_nacimiento} {self.fecha_fallecimiento} {self.activo} {self.activo} {self.creado}' 
    
    
class Frase(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='frases')
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return f'"{self.texto[:50]}..." - {self.autor.nombre}'