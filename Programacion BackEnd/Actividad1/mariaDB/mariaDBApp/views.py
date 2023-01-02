from django.shortcuts import render
from mariaDBApp.models import Reserva

# Create your views here.

# Vista Para Visualizar las Reservas en una Lista.
def reservaData(request):
    # Obtiene reservas desde base de datos
    reservas = Reserva.objects.all()
    data ={'reservas' : reservas}
    return render(request, 'templatesApp/lista_reservas.html')#, data)

# Vista Inicial.
def vistaInicial(request):
    return render(request, 'templatesApp/template_inicial.html')

# Formulario de Reserva.
def renderFormulario(request):
    return render(request, 'templatesApp/agregar_reserva.html')

# Vista Eliminar Reserva.
def eliminarReserva(request, id):
    # Obtenemos el id de la reserva a eliminar
    reserva = Reserva.objects.get(id = id)
    data ={'reserva' : reserva}
    reserva.delete()
    return render(request, 'templatesApp/reserva_eliminada.html')#, data)


# Vista Actualizar Reserva
def actualizarReserva(request, id):
    reserva = Reserva.objects.get(id=id)
    data = { 
        'reserva': reserva 
        }
    return render(request, 'templatesApp/actualizar_reserva.html')#, data)

# Vista de Reserva ya Actualizada.
def reserva_actualizada(request):
    id = int(request.POST['id'])
    p_nombre = request.POST['txt_nombre']
    p_fecha = request.POST['txt_fecha']
    p_hora = request.POST['txt_hora']
    p_cantidad = request.POST['txt_cantidad']
    p_telefono = request.POST['txt_telefono']
    p_observacion = request.POST['txt_observacion']

    reserva = Reserva.objects.get(id=id)
    reserva.nombre = p_nombre
    reserva.fecha = p_fecha
    reserva.hora = p_hora
    reserva.cantidad = p_cantidad
    reserva.telefono = p_telefono
    reserva.observacion = p_observacion
    reserva.save()
    return render(request,'templatesAPP/reserva_actualizada.html')


#Agregar una nueva Reserva
def agregarReserva(request):
    # obtenemos los datos recibidos con el metodo POST desde formulario ingreso
    p_nombre = request.POST['txt_nombre']
    p_fecha = request.POST['txt_fecha']
    p_hora = request.POST['txt_hora']
    p_cantidad = request.POST['txt_cantidad']
    p_telefono = request.POST['txt_telefono']
    p_observacion = request.POST['txt_observacion']

    # creamos un objeto de una reserva
    reserva = Reserva(nombre = p_nombre,
                      fecha = p_fecha,
                      hora = p_hora,
                      cantidad = p_cantidad,
                      telefono = p_telefono,
                      observacion = p_observacion)

    # agregamos la base de datos
    reserva.save()
    
    # redireccionamos a archivo en plantilla
    return render(request,'templatesAPP/reserva_creada.html')
