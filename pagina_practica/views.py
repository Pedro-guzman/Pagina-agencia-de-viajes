from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {})

def bonampak(request):
    return render(request, 'bonampak.html', {})

def cañon(request):
    return render(request, 'cañon.html', {})

def casa(request):
    return render(request, 'casa.html', {})

def ciapa(request):
    return render(request, 'ciapa.html', {})

def san(request):
    return render(request, 'san.html', {})

def dos(request):
    return render(request, 'dos.html', {})

def promo(request):
    return render(request, 'promo.html', {})

def avion(request):
    return render(request, 'avion.html', {})

def tematicos(request):
    return render(request, 'tematicos.html', {})

def sol(request):
    return render(request, 'sol.html', {})

def tours(request):
    return render(request, 'tours.html', {})

def top(request):
    return render(request, 'top.html', {})

def guia(request):
    return render(request, 'guia.html', {})

def cafe(request):
    return render(request, 'cafe.html', {})

def mapas(request):
    return render(request, 'mapas.html', {})

def direccion(request):
    return render(request, 'direccion.html', {})

def contform(request):
    return render(request, 'contform.html', {})

def mapa(request):
    return render(request, 'mapa.html', {})

def regisform(request):
    return render(request, 'regisform.html', {})

def sesionform(request):
    return render(request, 'sesionform.html', {})

def terminos(request):
    return render(request, 'terminos.html', {})

def aviso(request):
    return render(request, 'aviso.html', {})
#formularios
# La función goal toma un objeto 'request' como parámetro. Este objeto representa la solicitud HTTP que llega al servidor.

def goal(request):
    # Se verifica si el método de la solicitud no es GET. Si no es GET, significa que la solicitud no es válida para este bloque de código.
    if request.method != 'GET':
        return HttpResponse('el metodo post no esta soportado')
        # Si la solicitud no es GET, se intenta obtener el valor asociado con la clave 'name' de los parámetros GET de la solicitud.
    name = request.GET['name']

    # La siguiente línea de código se ejecuta independientemente de si la solicitud es GET o no.
    # Se renderiza la plantilla 'success.html' y se pasa el diccionario {'name': name} como contexto. 
    # Este diccionario se utiliza para proporcionar datos a la plantilla, como el valor de 'name' obtenido de la solicitud GET.

    return render(request, 'success.html', {'name': name})

def goal1(request):
   
    if request.method != 'GET':
        return HttpResponse('el metodo post no esta soportado')
       
    name = request.GET['name']
    return render(request, 'exitoregis.html', {'name': name})

def goal2(request):
   
    if request.method != 'GET':
        return HttpResponse('el metodo post no esta soportado')
       
    name = request.GET['name']
    return render(request, 'exitocontac.html', {'name': name})

def postform(request):
    return render(request, "postform.html", {})

def postgoal(request):
    if request.method != 'POST':
        return HttpResponse("El metodo GET no est soportado por esta ruta")
    info = request.POST['info']
    return render(request, "postsuccess.html", {"info": info})