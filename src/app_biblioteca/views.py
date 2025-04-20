from django.contrib.auth.decorators import login_required, login_not_required

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Libro, Comic, Prestamo

# Usuarios nuevos
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

# Mensaje de logout
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.

def base(request):
    query = request.GET.get('q', '')  # lo que el usuario escribe en la búsqueda

    libros = Libro.objects.filter(disponible=True)
    comics = Comic.objects.filter(disponible=True)

    if query:
        libros = libros.filter(titulo__icontains=query)
        comics = comics.filter(titulo__icontains=query)

    context = {
        'libros': libros,
        'comics': comics,
        'query': query
    }
    return render(request, 'base.html', context)

def lista_libros(request):
    query = request.GET.get('q', '')
    libros = Libro.objects.filter(disponible=True)

    if query:
        libros = libros.filter(titulo__icontains=query)

    return render(request, 'app_biblioteca/lista_libros.html', {
        'libros': libros,
        'query': query,
    })


def lista_comics(request):
    query = request.GET.get('q', '')
    comics = Comic.objects.filter(disponible=True)

    if query:
        comics = comics.filter(titulo__icontains=query)

    return render(request, 'app_biblioteca/lista_comics.html', {
        'comics': comics,
        'query': query,
    })


#@login_required
def prestar(request, tipo, item_id):
    if tipo == "libro":
        item = get_object_or_404(Libro, id=item_id)
    elif tipo == "comic":
        item = get_object_or_404(Comic, id=item_id)
    else:
        return redirect('app_autores:base')

    if item.disponible:
        Prestamo.objects.create(usuario=request.user, libro=item if tipo == "libro" else None, comic=item if tipo == "comic" else None)
        item.disponible = False
        item.save()

    return redirect('app_autores:base')

#@login_required
def mis_prestamos(request):
    prestamos = Prestamo.objects.filter(usuario=request.user).order_by('-fecha_prestamo')
    return render(request, 'app_biblioteca/mis_prestamos.html', {'prestamos': prestamos})

#@login_required
def devolver(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, id=prestamo_id, usuario=request.user, devuelto=False)

    if prestamo.libro:
        prestamo.libro.disponible = True
        prestamo.libro.save()
    elif prestamo.comic:
        prestamo.comic.disponible = True
        prestamo.comic.save()

    prestamo.devuelto = True
    prestamo.fecha_devolucion = timezone.now()
    prestamo.save()

    return redirect('app_biblioteca:mis_prestamos')

# Creación de usuario
@login_not_required
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente
            return redirect('app_autores:base')
    else:
        form = UserCreationForm()
    
    return render(request, 'app_biblioteca/signup.html', {'form': form})

# Vista mensaje cierre de sesión
def logout_view(request):
    logout(request)
    messages.success(request, "Sesión cerrada con éxito.")
    return redirect('app_autores:base')