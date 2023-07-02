from django.shortcuts import render, redirect
from .models import Producto, Comuna, Categoria, Region
from django.contrib import messages

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
    return render(request, template_name)

def pedidos(request):

    return render(request, 'core/WEB/ApartadoUsuario/misPedidos.html')

def usuario(request):

    return render(request, 'core/WEB/ApartadoUsuario/principalUsuario.html')

def registro_bike(request):

    return render(request, 'core/WEB/ApartadoUsuario/registro_bike.html')


def registro_usuario(request):
    comunas         = Comuna.objects.all
    template_name   = 'core/WEB/ApartadoUsuario/registro_usuario.html'
    context         = {"comunas":comunas}

    return render(request, template_name, context)

def registro_usuario(request):
    datos ={
        'form': NewUserForm()
    }
    if (request.method =='POST'):
        formulario = NewUserForm(request.POST)
        if (formulario.is_valid):
            formulario.save() 
        else:
            datos["comuna"] = Comuna.objects.all()
    return render(request, template_name, datos)

def seguimiento_envio(request):

    return render(request, 'core/WEB/ApartadoUsuario/seguimiento_envio.html')

# Apartado Contactanos

def contactanos(request):

    return render(request, 'core/WEB/Contactanos/contactanos.html')

# Apartado Productos

def carritoCompras(request):

    return render(request, 'core/WEB/Productos/carritoCompras.html')


def servicios(request):

    return render(request, 'core/WEB/Productos/servicios.html')

def form_usuario(request):
    return render(request, 'core/WEB/ApartadoUsuario/registro_usuario.html')

def buscar_categorias(request, slug):
    template_name   = 'core/WEB/Productos/list-products-categories.html'
    cat             = Categoria.objects.get(slug=slug)
    categorias      = Categoria.objects.filter(activo=True)
    productos       = Producto.objects.filter(activo=True, categoria=cat)
    context         = {"productos":productos, "categorias":categorias}
    return render(request, template_name, context)

def search(request):
    template_name   = 'core/WEB/Productos/productosYservicios.html'
    q               = request.GET["q"]
    productos       = Producto.objects.filter(activo=True, nombre_icontains=q)
    categorias      = Categoria.objects.filter(activo=True)
    context         = {"productos": productos,"categorias":categorias}
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
    if slug in session["item"]:
        messages.error(request,"Producto ya exixste en el Carrito")
    else:
        session["items"].append(slug)
        session["price"] += product.precioProducto
        session["count"] += 1
        request.session["data"] = session
        messages.success(request, "Agregado Exitosamente.")
    return redirect("core:details", slug)


def mycart(request):
    template_name    = 'core/WEB/Productos/productosYservicios.html'
    sess             = request.session.get("data", {"items":[]})
    products         = Producto.objects.filter(activo=True, slug__in = sess["items"])
    categorias       = Categoria.objects.filter(activo=True)
    context          = {"productos":products, "categorias":categorias}
    return render(request, template_name, context)