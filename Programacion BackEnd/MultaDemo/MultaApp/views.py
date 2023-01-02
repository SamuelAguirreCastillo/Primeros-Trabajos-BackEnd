from django.shortcuts import render
from MultaApp.models import Multa, Infractor
import requests

#Agregar una nueva Reserva

def ingresarInfraccion(request):
    multas = Multa.objects.all()
    data = {'multas':multas}
    return render(request,'templatesApp/agregar_multa.html')#,data)

def crearInfraccion(request):
    # Obtenemos valores
    p_tipo_multa = request.POST['sel_multa']
    p_nombre = request.POST['txt_nombre']
    p_apellido = request.POST['txt_apellido']
    p_celular = request.POST['txt_celular']
    p_fecha = request.POST['txt_fecha']
    p_hora = request.POST['txt_hora']
    p_email = request.POST['txt_email']
    p_detalles = request.POST['txt_detalles']
    p_rut = request.POST['txt_rut']

    #Obtenemos el valor en UTM de la multa
    multa_asignada = Multa.objects.get(id = p_tipo_multa)
    valor_multa_utm = multa_asignada.valor

    # Consultamos Valor UTM
    response = generarRequests('https://mindicador.cl/api/utm/01-11-2022')
    r_utm = response.get('serie')[0]
    v_utm = r_utm.get('valor')

    #Calculamos la multa
    valor_multa_pesos = valor_multa_utm * v_utm

    #Agregamos la infraccion a la bd
    infractor = Infractor(
                          nombre = p_nombre, 
                          apellido = p_apellido,
                          rut = p_rut,
                          email = p_email,
                          celular = p_celular, 
                          fecha = p_fecha, 
                          hora = p_hora,  
                          detalles = p_detalles, 
                          multa_id = p_tipo_multa,
                          monto = valor_multa_pesos
                          )

    infractor.save()

    return render(request, 'templatesApp/multa_creada.html')

# Generar Requests 
def generarRequests(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()

# Consultamos valor de  UTM
def obtenerUTM(request):
    response = generarRequests('https://mindicador.cl/api/utm/01-11-2022')
    utm = response.get('serie')[0]
    data = {'utm' : utm.get('valor')}
    return render(request, 'templatesApp/utm.html', data)