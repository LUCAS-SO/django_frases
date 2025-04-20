from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    editorial = models.CharField(max_length=255, blank=True, null=True)
    anio_publicacion = models.IntegerField()
    isbn = models.CharField(max_length=13, unique=True)
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to="libros/", null=True, blank=True)

    def __str__(self):
        return self.titulo

class Comic(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    editorial = models.CharField(max_length=255, blank=True, null=True)
    anio_publicacion = models.IntegerField()
    numero = models.IntegerField()
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to="comics/", null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} - #{self.numero}"
    
class Prestamo(models.Model):
    # usuario: Relacionado con el modelo User de Django para saber quién tomó prestado el libro o cómic.
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.SET_NULL, null=True, blank=True)
    comic = models.ForeignKey(Comic, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=True, blank=True)
    devuelto = models.BooleanField(default=False)

    def __str__(self):
        item = self.libro if self.libro else self.comic
        return f"{self.usuario.username} - {item.titulo}"