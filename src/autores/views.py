from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_not_required
from .models import Autor, Frase
import random

# from django.views.decorators.http import require_POST

# Create your views here.


@login_not_required
def inicio(request):
    return render(request, 'base.html')


def presentacion(request):
    return render(request, 'presentacion.html')


@login_not_required
def autores(request):
    autores = Autor.objects.all()
    for autor in autores:
        # Se realizar el slogify y poder mostrar las imagenes
        autor.slug = slugify(autor.nombre)
        # Nota: Esto no guarda el slug en la base de datos, solo lo calcula temporalmente para usarlo en el template.
    return render(request, 'app_autores/autores.html', {'autores': autores})


def autores_activos(request):
    autores = Autor.objects.filter(activo=True)
    return render(request, 'app_autores/activos.html', {'autores': autores})


def autores_inactivos(request):
    autores = Autor.objects.filter(activo=False)
    return render(request, 'app_autores/inactivos.html', {'autores': autores})


def cambiar_estado_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    autor.activo = not autor.activo
    autor.save()
    return HttpResponseRedirect(reverse('app_autores:autores'))


def autores_json(request):
    autores = get_list_or_404(Autor)
    autores_json = serializers.serialize('json', autores)
    return JsonResponse(autores_json, safe=False)


# Listado Json
#def autores_json(request):
#    autores = Autor.objects.all().values('id', 'nombre', 'nacionalidad', 'fecha_nacimiento', 'fecha_fallecimiento', 'activo')
#    return JsonResponse(list(autores), safe=False)

#def detalle_autor(request, autor_id):
#    autor = get_object_or_404(Autor, id=autor_id)
#    return render(request, 'app_autores/detalle.html', {'autor': autor})

#def borrar_autor(request, autor_id):
#    autor = get_object_or_404(Autor, id=autor_id)
#    autor.delete()
#    return HttpResponseRedirect(reversed('app_autores:autores'))


class AutorCreateViews(CreateView):
    model = Autor
    fields = ['nombre', 'nacionalidad', 'fecha_nacimiento',
              'fecha_fallecimiento', 'activo']
    success_url = reverse_lazy('app_autores:autores')
    template_name = 'crear.html'


class DetalleAutorView(DetailView):
    model = Autor
    template_name = 'app_autores/detalle.html'
    context_object_name = 'autor'
    pk_url_kwarg = 'autor_id'

    # Context para que se puedan ver las IMG en el template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        autor = context.get('autor')
        autor.slug = slugify(autor.nombre)
        return context


class AutorUpdateView(UpdateView):
    model = Autor
    fields = '__all__'
    template_name = 'crear.html'

    # Regresa al detalle
    def get_success_url(self):
        return reverse_lazy('app_autores:detalle_autor', kwargs={'autor_id': self.object.id})


class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'app_autores/borrar_autor.html'
    success_url = reverse_lazy('app_autores:autores')


# Views de Frases

@login_not_required
def frases_aleatorias(request):
    frases = list(Frase.objects.select_related('autor'))
    random.shuffle(frases)  # Mezclamos las frases
    for f in frases:
        f.autor.slug = slugify(f.autor.nombre)  # -> Para poder ver las IMG

    return render(request, 'app_autores/frases.html', {'frases': frases})


def frases_por_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    frases = autor.frases.all()
    autor.slug = slugify(autor.nombre)  # -> Para poder ver las IMG

    return render(request, 'app_autores/frases_autor.html', {'autor': autor, 'frases': frases})

# class FraseListViews(ListView):
#    # model = Frase # Se puede solicitar tanto model como query
#    queryset = Frase.objects.all()
#    template_name = 'app_autores/frases.html'
#    context_object_name = 'lista_frases' # Hace referecia a la relación del template


class FraseCreateViews(CreateView):
    model = Frase
    fields = ['autor', 'texto']
    success_url = reverse_lazy('app_autores:frases')
    template_name = 'crear.html'


# Realizado con GPT - Crea frases por autor
class FraseAutorCreateView(CreateView):
    """
    Vista para crear una frase asociada a un autor específico.
    - Recibe el `autor_id` por URL.
    - Asigna automáticamente el autor a la frase antes de guardarla.
    - Redirige a la lista de frases del autor después de guardar.
    """

    model = Frase
    fields = ['texto']  # No se pide el autor, se fija en `form_valid`
    template_name = 'app_autores/crear_frase_por_autor.html'

    # Valida el formulario para el autor de a cuerdo al pk=ID
    def form_valid(self, form):
        autor_id = self.kwargs['autor_id']
        form.instance.autor = get_object_or_404(Autor, pk=autor_id)
        return super().form_valid(form)

    # Redirecciona luego de guardar con exito
    def get_success_url(self):
        return reverse_lazy('app_autores:frases_autor', kwargs={'autor_id': self.kwargs['autor_id']})

    # Agrega datos al contexto, se agrega el autor (usando su ID) para poder mostrarlo como referencia visual (ejemplo en el titulo)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['autor'] = Autor.objects.get(pk=self.kwargs['autor_id'])
        return context


class FraseUpdateView(UpdateView):
    model = Frase
    fields = '__all__'
    template_name = 'crear.html'
    success_url = reverse_lazy('app_autores:frases')

class FraseDeleteView(DeleteView):
    model = Frase
    template_name = 'app_autores/borrar_frase.html'
    success_url = reverse_lazy('app_autores:frases')