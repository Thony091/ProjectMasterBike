from django.shortcuts import render
from .models import Producto

# Create your views here.
def index(request):

    return render(request, 'core/WEB/Principal/index.html')



def productos_servicios(request):
    productos = Producto.objects.all()

    datos = {
        'productos' : productos
    }

    return render(request, 'core/WEB/Productos/productosYservicios.html', datos)

# Apartado Productos

def historia(request):
    
    return render(request, 'core/WEB/ApartadoEmpresa/historia.html')

def metodos_envio(request):

    return render(request, 'core/WEB/ApartadoEmpresa/metodos_envio.html')

def nuestras_tiendas(request):

    return render(request, 'core/WEB/ApartadoEmpresa/nuestras_tiendas.html')

def preguntas_frecuentes(request):

    return render(request, 'core/WEB/ApartadoEmpresa/preguntas_frecuentes.html')

# Apartado Usuarios

def ayuda_contrasenia(request):

    return render(request, 'core/WEB/ApartadoUsuario/ayuda_contrasenia.html')

def login(request):

    return render(request, 'core/WEB/ApartadoUsuario/login.html')

def pedidos(request):

    return render(request, 'core/WEB/ApartadoUsuario/misPedidos.html')

def usuario(request):

    return render(request, 'core/WEB/ApartadoUsuario/principalUsuario.html')

def registro_bike(request):

    return render(request, 'core/WEB/ApartadoUsuario/registro_bike.html')

def registro_usuario(request):

    return render(request, 'core/WEB/ApartadoUsuario/registro_usuario.html')

def seguimiento_envio(request):

    return render(request, 'core/WEB/ApartadoUsuario/seguimiento_envio.html')

# Apartado Contactanos

def contactanos(request):

    return render(request, 'core/WEB/Contactanos/contactanos.html')

# Apartado Productos

def carritoCompras(request):

    return render(request, 'core/WEB/Productos/carritoCompras.html')

# def productosYservicios(request):

#     return render(request, 'core/WEB/Productos/productosYservicios.html')

def servicios(request):

    return render(request, 'core/WEB/Productos/servicios.html')

