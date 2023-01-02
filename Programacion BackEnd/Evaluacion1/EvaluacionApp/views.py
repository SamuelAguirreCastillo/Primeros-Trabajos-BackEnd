from ast import While
from inspect import _void
from urllib import request
from django.shortcuts import render

# Create your views here.

# View Para Visualizar Plantilla 'informacion.html'
def renderInformacion(request):
    return render(request, 'templatesApp/informacion.html')

# View Para Visualizar Plantilla 'formulario.html'
def renderFormulario(request):
    return render(request, 'templatesApp/formulario.html')

# View Para Visualizar Plantilla 'resultado.html' y los resultados de los metodos
def renderResultados(request):

    #Capturamos los Valores Recibidos via POST
    p_nombre_usuario = request.POST["txt_nombre_usuario"]
    p_apellido = request.POST["txt_apellido"]
    p_correo = request.POST["txt_correo"]
    p_celular = request.POST["txt_celular"]
    p_direccion = request.POST["txt_direccion"]
    p_codigo_postal = request.POST["txt_codigo_postal"]
    p_nombre_producto = request.POST["txt_nombre_producto"]
    p_cantidad = request.POST["txt_cantidad"]
    p_marca = request.POST["txt_marca"]
    p_modelo = request.POST["txt_modelo"]
    p_valor_transporte = request.POST["txt_valor_transporte"]
    p_valor_unitario = request.POST["txt_valor_unitario"]
    
    #If anidado que verifica que no haya valores nulos
    if len(p_nombre_usuario) > 0:
        if len(p_apellido) > 0:
            if len(p_correo) > 0:
                if len(p_celular) > 0:
                    if len(p_direccion) > 0:
                        if len(p_codigo_postal) > 0:
                            if len(p_nombre_producto) > 0:
                                if len(p_cantidad) > 0:
                                    if len(p_marca) > 0:
                                        if len(p_modelo) > 0:
                                            if len(p_valor_transporte) > 0:
                                                if len(p_valor_unitario) > 0:
                                                    #Funcion para calcular el valor inicial. Invocar función en python.
                                                    valor_inicial = calcular_valor_inicial(p_cantidad, p_valor_unitario)
                                                    #Funcion para calcular el valor cif. Invocar función en python.
                                                    valor_cif = calcular_valor_cif(p_cantidad, p_valor_transporte, p_valor_unitario)
                                                    #Funcion para calcular el valor iva. Invocar función en python.
                                                    valor_iva = calcular_iva(p_cantidad, p_valor_transporte, p_valor_unitario)
                                                    #Funcion para calcular el valor impuesto aduanero. Invocar función en python.
                                                    valor_aduanero = calcular_impuesto_aduanero(p_cantidad, p_valor_transporte, p_valor_unitario)


                                                    data ={ "valor_total" : f"{(valor_cif + valor_iva + valor_aduanero)/890:.2f}",
                                                            "valor_total_usd" : f"{valor_cif + valor_iva + valor_aduanero:.2f}",
                                                            "valor_inicial" : valor_inicial,
                                                            "valor_cif" : valor_cif,
                                                            "valor_iva" : f"{valor_iva:.2f}",
                                                            "valor_aduanero" : f"{valor_aduanero:.2f}",
                                                            "nombre_usuario" : p_nombre_usuario,
                                                            "apellido" : p_apellido,
                                                            "correo" : p_correo,
                                                            "celular" : p_celular,
                                                            "direccion" : p_direccion,
                                                            "codigo_postal" : p_codigo_postal,
                                                            "nombre_producto" : p_nombre_producto,
                                                            "marca" : p_marca,
                                                            "modelo" : p_modelo,
                                                            "valor_unitario" : p_valor_unitario,
                                                            "valor_transporte" : p_valor_transporte
                                                            }

                                                    return render(request, 'templatesApp/resultados.html', data) 
                                                else:
                                                    return renderInformacion(request)
                                            else:
                                                return renderInformacion(request)
                                        else:
                                            return renderInformacion(request)
                                    else:
                                        return renderInformacion(request)
                                else:
                                    return renderInformacion(request)
                            else:
                                return renderInformacion(request)
                        else:
                            return renderInformacion(request)
                    else:
                        return renderInformacion(request)
                else:
                    return renderInformacion(request)
            else:
                return renderInformacion(request)
        else:
            return renderInformacion(request)
    else:
        return renderInformacion(request)

#Metodo para Calcular el Valor Inicial (cantidad * valor unitario)
def calcular_valor_inicial(cantidad_producto, valor_producto):   
    valor_inical = int(cantidad_producto) * int(valor_producto)
    return valor_inical

#Metodo para Calcular el valor Cif (valor inicial * valor transporte)
def calcular_valor_cif(cantidad_producto, valor_transporte ,valor_producto):
    valor_cif = (int(cantidad_producto) * int(valor_producto)) + int(valor_transporte)
    return valor_cif

#Metodo para Calcular valor IVA (valor cif * 0.19(19%))
def calcular_iva(cantidad_producto, valor_transporte ,valor_producto):
    valor_iva = ((int(cantidad_producto) * int(valor_producto)) + int(valor_transporte)) * 0.19
    return valor_iva

#Metodo para Calcular valor impuesto aduanero (valor cif * 0.06(6%))
def calcular_impuesto_aduanero(cantidad_producto, valor_transporte ,valor_producto):
    valor_aduanero = ((int(cantidad_producto) * int(valor_producto)) + int(valor_transporte)) * 0.06
    return valor_aduanero



   