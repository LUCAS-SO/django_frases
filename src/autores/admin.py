from django.contrib import admin
from .models import Autor, Frase

# Register your models here.

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad', 'fecha_nacimiento', 'fecha_fallecimiento', 'activo')
    list_filter = ('activo', 'nacionalidad')
    search_fields = ('nombre',)

@admin.register(Frase)
class FraseAdmin(admin.ModelAdmin):
    list_display = ('autor', 'texto', 'fecha_creacion')
    search_fields = ('texto',)