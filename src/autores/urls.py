from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import (
    AutorCreateViews,
    AutorUpdateView,
    AutorDeleteView,
    DetalleAutorView,
    FraseCreateViews,
    FraseAutorCreateView,
    FraseUpdateView,
    FraseDeleteView,
)


app_name = 'app_autores'

urlpatterns = [
    # Registro
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # URLs Generales
    path('', views.inicio, name='base'),
    path('presentacion/', views.presentacion, name='presentacion'),
    path('autores/json/', views.autores_json, name='autores_json'),
    
    # URLs de Autores
    path('autores/', views.autores, name='autores'),
    path('autores/crear_autor/', AutorCreateViews.as_view(), name='crear_autor'),
    path('autores/<int:autor_id>/', DetalleAutorView.as_view(), name='detalle_autor'),
    path('autores/<int:pk>/modificar_autor/', AutorUpdateView.as_view(), name='modificar_autor'),
    path('autores/<int:pk>/borrar/', AutorDeleteView.as_view(), name='borrar_autor'),
    
    # Filtro Autores
    path('autores/activos/', views.autores_activos, name='autores_activos'),
    path('autores/inactivos/', views.autores_inactivos, name='autores_inactivos'),
    path('autores/<int:autor_id>/cambiar_estado/', views.cambiar_estado_autor, name='cambiar_estado_autor'),
    
    # URLs de Autores y Frases
    path('autores/<int:autor_id>/frases/', views.frases_por_autor, name='frases_autor'),
    path('autores/<int:autor_id>/crear_frase/', FraseAutorCreateView.as_view(), name='crear_frase_autor'),

    # URLs de Frases
    path('frases/', views.frases_aleatorias, name='frases'),
    path('frases/crear_frase/', FraseCreateViews.as_view(), name='crear_frase'),
    path('frases/<int:pk>/modificar_frase/', FraseUpdateView.as_view(), name="modificar_frase"),
    path('frases/<int:pk>/borrar/', FraseDeleteView.as_view(), name='borrar_frase'),
]
