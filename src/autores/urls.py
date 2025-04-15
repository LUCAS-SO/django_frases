from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import (
    FraseCreateViews,
    FraseAutorCreateView,
    AutorCreateViews,
    AutorUpdateView,
    AutorDeleteView,
    DetalleAutorView,
)


app_name = 'app_autores'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', views.inicio, name='base'),
    path('presentacion/', views.presentacion, name='presentacion'),
    path('autores/', views.autores, name='autores'),
    path('autores/crear_autor/', AutorCreateViews.as_view(), name='crear_autor'),
    path('autores/<int:pk>/borrar/', AutorDeleteView.as_view(), name='borrar_autor'),
    path('frases/', views.frases_aleatorias, name='frases'),
    path('frases/crear_frase/', FraseCreateViews.as_view(), name='crear_frase'),
    path('autores/<int:autor_id>/frases/', views.frases_por_autor, name='frases_autor'),
    path('autores/<int:autor_id>/crear_frase/', FraseAutorCreateView.as_view(), name='crear_frase_autor'),
    path('autores/<int:pk>/modificar_autor/', AutorUpdateView.as_view(), name='modificar_autor'),
    path('autores/activos/', views.autores_activos, name='autores_activos'),
    path('autores/inactivos/', views.autores_inactivos, name='autores_inactivos'),
    path('autores/json/', views.autores_json, name='autores_json'),
    #path('autores/<int:autor_id>/', views.detalle_autor, name='detalle_autor'),
    path('autor/<int:autor_id>/', DetalleAutorView.as_view(), name='detalle_autor'),
    path('autores/<int:autor_id>/borrar/', views.borrar_autor, name='borrar_autor'),
    path('autores/<int:autor_id>/cambiar_estado/', views.cambiar_estado_autor, name='cambiar_estado_autor'),
]
