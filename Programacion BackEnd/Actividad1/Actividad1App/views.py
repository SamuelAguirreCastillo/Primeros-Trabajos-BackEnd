from django.shortcuts import render


# Create your views here.


def tablaMultiplicar(request):
    numero_multiplicar = 2
    data = {"tabla0" : numero_multiplicar*0, 
            "tabla1" : numero_multiplicar*1, 
            "tabla2" : numero_multiplicar*2, 
            "tabla3" : numero_multiplicar*3, 
            "tabla4" : numero_multiplicar*4, 
            "tabla5" : numero_multiplicar*5, 
            "tabla6" : numero_multiplicar*6,
            "tabla7" : numero_multiplicar*7,
            "tabla8" : numero_multiplicar*8,
            "tabla9" : numero_multiplicar*9,
            "tabla10" : numero_multiplicar*10,
            "tabla11" : numero_multiplicar*11,
            "tabla12" : numero_multiplicar*12,
            "numero" : numero_multiplicar}

    return render(request, 'PlantillasApp/plantilla1.html', data)


def calculoPeso(request):
    edad = 9
    data = {"ideal" : edad*2+8,
            "edad" : edad}

    return render(request, 'PlantillasApp/plantilla2.html', data)

def valorCombustible(request):
    Valor93 = 1010
    Valor95 = 1099
    Valor97 = 1190
    VDiesel = 980
    Cantidad = 40000
    data = {"L93" : f"{Cantidad/Valor93:.2f}",
            "L95" : f"{Cantidad/Valor95:.2f}",
            "L97" : f"{Cantidad/Valor97:.2f}",
            "LDiesel" : f"{Cantidad/VDiesel:.2f}",
            "Cantidad" : Cantidad,
            "Com93" : Valor93,
            "Com95" : Valor95,
            "Com97" : Valor97,
            "Diesel" : VDiesel}
    return render(request, 'PlantillasApp/plantilla3.html', data)
