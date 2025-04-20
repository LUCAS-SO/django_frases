from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

app_name = 'app_biblioteca'

urlpatterns = [
    # Registro de Usuario
    path('registro/', views.signup, name='signup'),

    path('libros/', views.lista_libros, name='lista_libros'),
    path('comics/', views.lista_comics, name='lista_comics'),
    
    path('mis-prestamos/', views.mis_prestamos, name='mis_prestamos'),
    path('prestar/<str:tipo>/<int:item_id>/', views.prestar, name='prestar'),
    path('devolver/<int:prestamo_id>/', views.devolver, name='devolver'),
    
    # path('logout/', LogoutView.as_view(), name='logout'),
    #path('logout/', views.logout_view, name='logout'),
]