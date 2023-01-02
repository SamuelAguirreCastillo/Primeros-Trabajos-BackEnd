from django.shortcuts import render
from agendaApp.models import PersonaCita, PreguntaFrecuente
# Create your views here.

def index(request):
    return render(request, 'agendaApp/index.html')

def ingresar_cita(request):
    return render(request, 'agendaApp/ingresar_cita.html')


def confirmacion_cita(request):
    p_nombre = request.POST['txt_nombre']
    p_apellidos = request.POST['txt_apellidos']
    p_email = request.POST['txt_email']
    p_celular = int(request.POST['txt_celular'])
    p_fecha = request.POST['txt_fecha']
    p_hora = request.POST['txt_hora']
    p_motivo = request.POST['txt_motivo']

    PersonaCita(nombre = p_nombre, apellido = p_apellidos, email = p_email, celular = p_celular,
          fecha = p_fecha, hora = p_hora, motivo = p_motivo).save()
    
    data = {'nombre' : p_nombre,
            'apellidos' : p_apellidos,
            'fecha' : p_fecha,
            'hora' : p_hora}
    return render(request, 'agendaApp/confirmacion_cita.html', data)


def filtrar_citas(request):
    return render(request, 'agendaApp/filtrar_citas.html')

def tabla_citas(request):
    p_fecha_cita = request.POST['txt_fecha']
    citas = PersonaCita.objects.filter(fecha=p_fecha_cita)
    data = {"citas": citas}
    return render(request, 'agendaApp/tabla_citas.html', data)


def inicio_admin(request):
    return render(request, 'agendaApp/inicio_admin.html')


def preguntas_frecuentes(request):
    preguntas_frecuentes = PreguntaFrecuente.objects.all()
    data = {'preguntas' : preguntas_frecuentes }
    return render(request, 'agendaApp/preguntas_frecuentes.html', data)

def editar_preguntas_frecuentes(request):
    preguntas_frecuentes = PreguntaFrecuente.objects.all()
    data = {'preguntas' : preguntas_frecuentes }
    return render(request, 'agendaApp/editar_preguntas_frecuentes.html', data)

def eliminar_pregunta_frecuente(request):
    id_eliminar = request.GET.get('id')
    pregunta = PreguntaFrecuente.objects.get(id = id_eliminar)
    data = {'pregunta': pregunta}
    return render(request, 'agendaApp/eliminar_pregunta_frecuente.html', data)

def confirmacion_eliminacion_pregunta(request):
    id_eliminar = request.GET.get('id')
    PreguntaFrecuente.objects.get(id = id_eliminar).delete()
    return render(request, 'agendaApp/confirmar_eliminacion_pregunta.html')

def modificar_pregunta(request):
    id_editar = request.GET.get('id')
    pregunta = PreguntaFrecuente.objects.get(id = id_editar)
    data = {"pregunta" : pregunta}
    return render(request, 'agendaApp/modificar_pregunta.html', data)

def confirmar_edit(request):
    id_editar = request.GET.get('id')
    p_titulo = request.POST['txt_titulo']
    p_descripcion = request.POST['txt_descripcion']

    pregunta = PreguntaFrecuente.objects.get(id = id_editar)
    pregunta.titulo = p_titulo
    pregunta.descripcion = p_descripcion
    pregunta.save()
    return render(request, 'agendaApp/confirmar_edit.html')

def form_agregar_pregunta(request):
    return render(request, 'agendaApp/form_pregunta.html')

def confirmar_agregar_pregunta(request):
    p_titulo = request.POST['txt_titulo']
    p_descripcion = request.POST['txt_descripcion']

    PreguntaFrecuente(titulo = p_titulo, descripcion = p_descripcion).save()
    return render(request, 'agendaApp/confirmar_agregar_pregunta.html')

def eliminar_cita(request):
    id_eliminar = request.GET.get('id')
    cita = PersonaCita.objects.get(id = id_eliminar)
    data = {'cita': cita}
    return render(request, 'agendaApp/eliminar_cita.html', data)

def confirmar_eliminacion_cita(request):
    id_eliminar = request.GET.get('id')
    PersonaCita.objects.get(id = id_eliminar).delete()

    return render(request, 'agendaApp/confirmar_eliminacion_cita.html')