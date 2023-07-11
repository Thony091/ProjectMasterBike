from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Producto, Comuna, Categoria
from .forms import ContactoForm, ClienteCreationForm


template_index   = 'core/WEB/Principal/index.html'
template_redir   = 'core:index'
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

def user_login(request):
    template_name   ='core/WEB/ApartadoUsuario/login.html'
    if request.method =='GET':
        return render(request, template_name,{
            'form': AuthenticationForm
        })
    else:
        #Autenticamos el usuario y el password con el motodo "Authenticate"
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None: #pregunta si el usuario no se encontro en             
            return render(request, template_name,{'form': AuthenticationForm,
                        'error': 'usuario o contraseña incorrecta'})
        else:
            login(request, user)
            return redirect('core:index')

def pedidos(request):

    return render(request, 'core/WEB/ApartadoUsuario/misPedidos.html')

def usuario(request):

    return render(request, 'core/WEB/ApartadoUsuario/principalUsuario.html')

def registro_bike(request):
    
    return render(request, 'core/WEB/ApartadoUsuario/registro_bike.html')


def registro_usuario(request):
    template_name = 'core/WEB/ApartadoUsuario/registro_usuario.html'
    data = {
        'form': ClienteCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = ClienteCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            try:
                user_creation_form.save()
                messages.success(request, "Usuario Registrado.")
                user = authenticate(username=user_creation_form.cleaned_data['username'],password=user_creation_form.cleaned_data['password1'])
                login(request, user)
                return redirect('core:index')
            except IntegrityError:
                return render(request, template_name, {"form": ClienteCreationForm, "error": "Usuario ya existe."})
        else:
            data['form'] = user_creation_form

    return render(request, template_name, data)

def seguimiento_envio(request):
    
    return render(request, 'core/WEB/ApartadoUsuario/seguimiento_envio.html')

# Apartado Contactanos

def contactanos(request):
    template_name = 'core/WEB/Contactanos/contactanos.html'
    datos ={
        'form': ContactoForm()
    }
    if (request.method =='POST'):
        formulario = ContactoForm(request.POST)
        if (formulario.is_valid):
            formulario.save()
            messages.success(request, "Su mensaje ha sido enviado, le responderemos a la brevedad, gracias.")        
        return render(request, template_name, datos)
    else:
        return render(request, template_name, datos)

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
    product     = Producto.objects.get(slug=slug)
    initial     = {"items":[], "price": 0, "count": 0}
    session     = request.session.get("data", initial)
    if slug in session["items"]:
        messages.error(request,"Producto ya existe en el Carrito")
    else:
        session["items"].append(slug)
        session["price"] += product.precioProducto
        session["count"] += 1
        request.session["data"] = session
        messages.success(request, "Agregado Exitosamente.")
    return redirect("core:detail", slug)

def eliminar_producto(request,slug):
    template_name     = 'core/WEB/Productos/carritoCompras.html'
    product           = Producto.objects.get(slug=slug)
    sess              = request.session.get("data", {"items":[]})
    session           = request.session.get("data", sess)
    session["items"].remove(slug)
    session["price"] -= product.precioProducto
    session["count"] -= 1
    request.session["data"] = session
    messages.success(request, "Producto eliminado Exitosamente.")
    newSess           = request.session.get("data", {"items":[]})
    products          = Producto.objects.filter(activo=True, slug__in = sess["items"])
    context           = {"productos":products}
    return render(request, template_name, context)

@login_required 
def mycart(request):
    template_name    = 'core/WEB/Productos/carritoCompras.html'
    sess             = request.session.get("data", {"items":[]})
    products         = Producto.objects.filter(activo=True, slug__in = sess["items"])
    categorias       = Categoria.objects.filter(activo=True)
   
    context          = {"productos":products, "categorias":categorias}
    return render(request, template_name, context)