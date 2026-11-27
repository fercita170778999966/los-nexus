from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import Usuario, Servicio, UbicacionCecytem, Incidencia, Sugerencia
from .forms import RegistroForm, IncidenciaForm, SugerenciaForm, PerfilForm, ServicioForm




class InicioView(TemplateView):
    template_name = 'inicio.html'


class UbicacionesListView(ListView):
    model = UbicacionCecytem
    template_name = 'ubicaciones.html'
    context_object_name = 'ubicaciones'


class ServiciosListView(ListView):
    model = Servicio
    template_name = 'servicios.html'
    context_object_name = 'servicios'


class AdminUsuariosListView(ListView):
    model = Usuario
    template_name = 'admin_usuarios.html'
    context_object_name = 'usuarios'


class AdminCatalogoListView(ListView):
    model = Servicio
    template_name = 'admin_catalogo.html'
    context_object_name = 'servicios'

class CrearServicioView(CreateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'servicio_form.html'
    success_url = reverse_lazy('admin_catalogo')

class EditarServicioView(UpdateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'servicio_form.html'
    success_url = reverse_lazy('admin_catalogo')

class EliminarServicioView(DeleteView):
    model = Servicio
    success_url = reverse_lazy('admin_catalogo')


class AdminIncidenciasListView(ListView):
    model = Incidencia
    template_name = 'admin_incidencias.html'
    context_object_name = 'incidencias'

class EliminarIncidenciaView(DeleteView):
    model = Incidencia
    success_url = reverse_lazy('admin_incidencias')


class AdminBuzonListView(ListView):
    model = Sugerencia
    template_name = 'admin_buzon.html'
    context_object_name = 'sugerencias'




def iniciar_sesion(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        clave = request.POST.get('password')
        user = authenticate(username=correo, password=clave)
        if user:
            login(request, user)

            
            usuario_perfil = Usuario.objects.filter(id=user.id).first()
            if user.is_superuser or (usuario_perfil and usuario_perfil.rol == 'admin'):
                return redirect('admin_metricas')
            return redirect('panel_estudiante')
    return render(request, 'login.html')



def registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.username = form.cleaned_data['email']
            usuario.set_password(form.cleaned_data['password'])
            usuario.rol = 'estudiante'
            usuario.save()
            login(request, usuario)
            return redirect('panel_estudiante')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')


def panel_estudiante(request):
    usuario_actual = get_object_or_404(Usuario, id=request.user.id)
    mis_reportes = Incidencia.objects.filter(usuario=usuario_actual).count()
    mis_sugerencias = Sugerencia.objects.filter(usuario=usuario_actual).count()
    return render(request, 'panel_estudiante.html', {
        'mis_reportes': mis_reportes,
        'mis_sugerencias': mis_sugerencias
    })


def reportar_problema(request):
    usuario_actual = get_object_or_404(Usuario, id=request.user.id)
    if request.method == 'POST':
        form = IncidenciaForm(request.POST)
        if form.is_valid():
            incidencia = form.save(commit=False)
            incidencia.usuario = usuario_actual
            incidencia.save()
            return redirect('reportar_problema')
    else:
        form = IncidenciaForm()
        
    historial = Incidencia.objects.filter(usuario=usuario_actual)
    return render(request, 'reportar.html', {'form': form, 'historial': historial})


def sugerencias(request):
    usuario_actual = get_object_or_404(Usuario, id=request.user.id)
    if request.method == 'POST':
        form = SugerenciaForm(request.POST)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.usuario = usuario_actual
            idea.save()
            return redirect('sugerencias')
    else:
        form = SugerenciaForm()
        
    mis_ideas = Sugerencia.objects.filter(usuario=usuario_actual)
    return render(request, 'sugerencias.html', {'form': form, 'mis_ideas': mis_ideas})


def perfil(request):
    usuario_actual = get_object_or_404(Usuario, id=request.user.id)
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=usuario_actual)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = PerfilForm(instance=usuario_actual)
    return render(request, 'perfil.html', {'form': form})


def admin_metricas(request):
    datos = {
        'usuarios': Usuario.objects.count(),
        'reportes': Servicio.objects.count(),
        'incidencias': Incidencia.objects.count(),
        'sugerencias': Sugerencia.objects.count(),
    }
    return render(request, 'admin_metricas.html', datos)


def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if not usuario.es_protegido:
        usuario.delete()
    return redirect('admin_usuarios')
