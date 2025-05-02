from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Actividad, UsuarioInscrito, Monitor, Sala, ResponsableSala
from .forms import ActividadForm, UsuarioForm, MonitorForm, SalaForm, ResponsableForm

def inicio(request):
    return render(request, 'base.html')

def lista_actividades(request):
    actividades = Actividad.objects.all()
    monitores = Monitor.objects.all()

    tipo = request.GET.get('tipo')
    if tipo:
        actividades = actividades.filter(tipo__iexact=tipo)

    monitor_id = request.GET.get('monitor')
    if monitor_id:
        actividades = actividades.filter(monitor__id=monitor_id)

    return render(request, 'actividades/lista.html', {
        'actividades': actividades,
        'monitores': monitores
    })

def detalle_actividad(request, id):
    actividad = get_object_or_404(Actividad, id=id)
    return render(request, 'actividades/detalle.html', {'actividad': actividad})

def crear_actividad(request):
    form = ActividadForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'actividades/formulario.html', {'formulario': form, 'titulo': 'Registrar Actividad'})

def editar_actividad(request, id):
    actividad = get_object_or_404(Actividad, id=id)
    if request.method == 'POST':
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            return redirect('detalle_actividad', id=actividad.id)
    else:
        form = ActividadForm(instance=actividad)
    return render(request, 'actividades/formulario.html', {'form': form})

def eliminar_actividad(request, id):
    actividad = get_object_or_404(Actividad, id=id)
    if request.method == 'POST':
        actividad.delete()
        return redirect('lista_actividades')
    return render(request, 'actividades/confirmar_eliminacion.html', {'actividad': actividad})

def lista_inscripciones(request, id):
    actividad = get_object_or_404(Actividad, id=id)
    usuarios = actividad.usuarios.all()
    return render(request, 'actividades/inscripciones.html', {'actividad': actividad, 'usuarios': usuarios})

def inscribir_usuario(request, id):
    actividad = get_object_or_404(Actividad, id=id)
    if request.method == 'POST':
        usuario_id = request.POST.get('usuario_id')
        usuario = get_object_or_404(UsuarioInscrito, id=usuario_id)
        actividad.usuarios.add(usuario)
        return redirect('lista_inscripciones', id=id)
    usuarios = UsuarioInscrito.objects.exclude(actividades=actividad)
    return render(request, 'actividades/inscribir.html', {'actividad': actividad, 'usuarios': usuarios})

def eliminar_inscripcion(request, id, usuario_id):
    actividad = get_object_or_404(Actividad, id=id)
    usuario = get_object_or_404(UsuarioInscrito, id=usuario_id)
    actividad.usuarios.remove(usuario)
    return redirect('lista_inscripciones', id=id)

def lista_usuarios(request):
    actividad_id = request.GET.get('actividad')
    if actividad_id:
        usuarios = UsuarioInscrito.objects.filter(actividades__id=actividad_id)
    else:
        usuarios = UsuarioInscrito.objects.all()

    return render(request, 'usuarios/lista.html', {'usuarios': usuarios})

def detalle_usuario(request, id):
    usuario = get_object_or_404(UsuarioInscrito, id=id)
    return render(request, 'usuarios/detalle.html', {'usuario': usuario})

def crear_usuario(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'usuarios/formulario.html', {'formulario': form, 'titulo': 'Registrar Usuario'})

def editar_usuario(request, id):
    usuario = get_object_or_404(UsuarioInscrito, id=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('detalle_usuario', id=id)
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/formulario.html', {'form': form})

def eliminar_usuario(request, id):
    usuario = get_object_or_404(UsuarioInscrito, id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')
    return render(request, 'usuarios/confirmar_eliminacion.html', {'usuario': usuario})

def lista_monitores(request):
    monitores = Monitor.objects.all()
    return render(request, 'monitores/lista.html', {'monitores': monitores})

def detalle_monitor(request, id):
    monitor = get_object_or_404(Monitor, id=id)
    return render(request, 'monitores/detalle.html', {'monitor': monitor})

def crear_monitor(request):
    form = MonitorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'monitores/formulario.html', {'formulario': form, 'titulo': 'Registrar Monitor'})

def editar_monitor(request, id):
    monitor = get_object_or_404(Monitor, id=id)
    if request.method == 'POST':
        form = MonitorForm(request.POST, instance=monitor)
        if form.is_valid():
            form.save()
            return redirect('detalle_monitor', id=id)
    else:
        form = MonitorForm(instance=monitor)
    return render(request, 'monitores/formulario.html', {'form': form})

def eliminar_monitor(request, id):
    monitor = get_object_or_404(Monitor, id=id)
    if request.method == 'POST':
        monitor.delete()
        return redirect('lista_monitores')
    return render(request, 'monitores/confirmar_eliminacion.html', {'monitor': monitor})

def lista_salas(request):
    salas = Sala.objects.all()
    return render(request, 'salas/lista.html', {'salas': salas})

def detalle_sala(request, id):
    sala = get_object_or_404(Sala, id=id)
    return render(request, 'salas/detalle.html', {'sala': sala})

def crear_sala(request):
    form = SalaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'salas/formulario.html', {'formulario': form, 'titulo': 'Registrar Sala'})

def editar_sala(request, id):
    sala = get_object_or_404(Sala, id=id)
    if request.method == 'POST':
        form = SalaForm(request.POST, instance=sala)
        if form.is_valid():
            form.save()
            return redirect('detalle_sala', id=id)
    else:
        form = SalaForm(instance=sala)
    return render(request, 'salas/formulario.html', {'form': form})

def eliminar_sala(request, id):
    sala = get_object_or_404(Sala, id=id)
    if request.method == 'POST':
        sala.delete()
        return redirect('lista_salas')
    return render(request, 'salas/confirmar_eliminacion.html', {'sala': sala})