from django.shortcuts import render
from .models import Producto

# Create your views here.
def index(request):

    return render(request, 'core/WEB/Principal/index.html')



def productosYServicios(request):
    productos = Producto.objects.all()

    datos = {
        'productos' : productos
    }

    return render(request, 'core/WEB/Productos/productosYservicios.html', datos)