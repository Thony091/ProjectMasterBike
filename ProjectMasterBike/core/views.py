from django.shortcuts import render, redirect
from .models import Producto, Comuna, Categoria
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import UsuarioForm
from django.db import IntegrityError


template_index   = 'core/WEB/Principal/index.html'
# Create your views here.
def index(request):
    template_name   = 'core/WEB/Principal/index.html'

    return render(request, template_name)


def productos_servicios(request):
    template_name   ='core/WEB/Productos/productosYservicios.html'
    categorias      = Categoria.objects.filter(activo=True)
    productos       = Producto.objects.filter(activo=True)
    context         = {"productos":productos, "categorias":categorias}
    return render(request, template_name, context)

# Apartado Informaciones

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
    template_name   ='core/WEB/ApartadoUsuario/login.html'
    if request.method =='GET':
        return render(request, template_name,{
            'form': AuthenticationForm
        })
    else:
        authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, template_name,{
            'form': AuthenticationForm,
            'error': 'username or password is incorrect'
            })
        else:
            return redirect(template_index)
        return render(request, template_name,{
            'form': AuthenticationForm
        })


def pedidos(request):

    return render(request, 'core/WEB/ApartadoUsuario/misPedidos.html')

def usuario(request):

    return render(request, 'core/WEB/ApartadoUsuario/principalUsuario.html')

def registro_bike(request):

    return render(request, 'core/WEB/ApartadoUsuario/registro_bike.html')


def registro_usuario(request):
    template_name ='core/WEB/ApartadoUsuario/registro_usuario.html'
    datos ={
        'form': UsuarioForm()
    }
    if (request.method =='POST'):
        formulario = UsuarioForm(request.POST)
        if (formulario.is_valid):
            formulario.save()
        login(request, usuario)
        return redirect('')        
    else:
        datos["comunas"] = Comuna.objects.all()
    return render(request, template_name, datos)
    # return JsonResponse(datos)

def seguimiento_envio(request):
    
    return render(request, 'core/WEB/ApartadoUsuario/seguimiento_envio.html')

# Apartado Contactanos

def contactanos(request):

    return render(request, 'core/WEB/Contactanos/contactanos.html')

# Apartado Productos

# def carritoCompras(request):

#     return render(request, 'core/WEB/Productos/carritoCompras.html')

# def productosYservicios(request):

#     return render(request, 'core/WEB/Productos/productosYservicios.html')

def servicios(request):

    return render(request, 'core/WEB/Productos/servicios.html')

def form_usuario(request):
    return render(request, 'core/WEB/ApartadoUsuario/registro_usuario.html')

def signout(request):
    logout(request)
    return redirect('/')



def buscar_categorias(request, slug):
    template_name   = 'core/WEB/Productos/list-products-categories.html'
    cat             = Categoria.objects.get(slug=slug)
    categorias      = Categoria.objects.filter(activo=True)
    productos       = Producto.objects.filter(activo=True, categoria=cat)
    context         = {"productos":productos, "categorias":categorias}
    return render(request, template_name, context)

def detail(request, slug):
    if Producto.objects.filter(activo=True, slug=slug).exists():
        template_name   = 'core/WEB/Productos/detail.html'
        producto        = Producto.objects.get(activo=True, slug=slug)
        categorias      = Categoria.objects.filter(activo=True)
        context         = {"producto":producto, "categorias":categorias}
        return render(request, template_name, context)

def cart(request,slug):
    template_name    = 'core/WEB/Productos/carritoCompras.html'
    product     = Producto.objects.get(slug=slug)

    initial     = {"items":[], "price": 0, "count": 0}
    session     = request.session.get("data", initial)
    if slug in session["items"]:
        messages.error(request,"Producto ya exixste en el Carrito")
    else:
        session["items"].append(slug)
        session["price"] += product.precioProducto
        session["count"] += 1
        request.session["data"] = session
        messages.success(request, "Agregado Exitosamente.")
    return redirect("core:detail", slug)


def mycart(request):
    template_name    = 'core/WEB/Productos/carritoCompras.html'
    sess             = request.session.get("data", {"items":[]})
    products         = Producto.objects.filter(activo=True, slug__in = sess["items"])
    categorias       = Categoria.objects.filter(activo=True)
   
    context          = {"productos":products, "categorias":categorias}
    return render(request, template_name, context)