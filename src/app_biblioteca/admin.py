from django.contrib import admin
from .models import Libro, Comic, Prestamo

# Register your models here.

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    # list_display: Define las columnas visibles en la lista del admin.
    list_display = ('titulo', 'autor', 'anio_publicacion', 'disponible', 'imagen')
    # search_fields: Permite buscar por título, autor e ISBN (solo para libros).
    search_fields = ('titulo', 'autor', 'isbn')
    # list_filter: Agrega filtros en la barra lateral para facilitar la búsqueda.
    list_filter = ('disponible', 'anio_publicacion')

@admin.register(Comic)
class ComicAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'numero', 'anio_publicacion', 'disponible', 'imagen')
    search_fields = ('titulo', 'autor')
    list_filter = ('disponible', 'anio_publicacion')

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'libro', 'comic', 'fecha_prestamo', 'fecha_devolucion', 'devuelto')
    search_fields = ('usuario__username', 'libro__titulo', 'comic__titulo')
    list_filter = ('devuelto', 'fecha_prestamo', 'fecha_devolucion')