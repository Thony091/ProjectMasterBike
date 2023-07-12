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

#Método que renderiza la página y el contexto que se le enviará al llamar a la url vinculada a este método
def productos_servicios(request):
    template_name   ='core/WEB/Productos/productosYservicios.html'
    # variable que guardara todos los objetos de categorias filtrados por si estan activos
    categorias      = Categoria.objects.filter(activo=True)
    # variable que guardara todos los objetos de productos filtrados por si estan activos
    productos       = Producto.objects.filter(activo=True)
    # variable que guardara un diccionario con la información filtrada en los pasos anteriores y los enviara a la pagina indicada para ser usada
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
#Método para logear
def user_login(request):
    template_name   ='core/WEB/ApartadoUsuario/login.html'
    if request.method =='GET':#Cuando el metodo sea "Get" (cuando llamas a la pagina) enviará la la "forma" para ser implementada
        return render(request, template_name,{
            'form': AuthenticationForm
        })
    else: #al ser "else" se entiende que el método es "post"
        #Autenticamos el usuario y el password con el método "Authenticate"(método de django) y lo guardamos en una variable
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None: #pregunta si el usuario no se encontro en bd reenvia el formularia y un mensaje de error.             
            return render(request, template_name,{'form': AuthenticationForm,
                        'error': 'usuario o contraseña incorrecta'})
        else:#si encuentra el usuario lo logueara y redireccionara al index
            login(request, user)
            return redirect('core:index')

# Método que ayudara a deslogear de la cuenta (método de django)
def signout(request):
    logout(request) #
    return redirect('/')

def pedidos(request):

    return render(request, 'core/WEB/ApartadoUsuario/misPedidos.html')

def usuario(request):

    return render(request, 'core/WEB/ApartadoUsuario/principalUsuario.html')

def registro_bike(request):
    
    return render(request, 'core/WEB/ApartadoUsuario/registro_bike.html')

#Método para registrar usuario
def registro_usuario(request):
    template_name = 'core/WEB/ApartadoUsuario/registro_usuario.html'
    # variable que guarda la "forma" para la creacion de un usuario, se podra renderizar cuando se invoque la url asociada a este método
    data = {
        'form': ClienteCreationForm()
    }

    if request.method == 'POST':
        # variable que guarda la data enviada desde el front con el "method='post'" 
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

def servicios(request):
    return render(request, 'core/WEB/Productos/servicios.html')

#Método para agrupar productos por el tipo de categoria enviado desde el front cuando pulsan el tipo de categoria que se prefiere (llega por el slug)
def buscar_categorias(request, slug):
    template_name   = 'core/WEB/Productos/list-products-categories.html'
    #variable que guarda los objetos con el nombre que se envio al dar click en la variable "slug"
    cat             = Categoria.objects.get(slug=slug) 
    # variable que guardara todos los objetos de categorias filtrados por si estan activos
    categorias      = Categoria.objects.filter(activo=True)
    # variable que guardara todos los objetos de categorias filtrados por si estan activos y sean de la categoria guardad en la variable cat
    productos       = Producto.objects.filter(activo=True, categoria=cat)
    context         = {"productos":productos, "categorias":categorias}
    return render(request, template_name, context)

#Método para ver el detalle de un producto al pulsar en la fotografia o al agregar al carrito de compra 
def detail(request, slug):
    #el método preguntara si el producto enviado desde el front está activo y con el nombre almacenado en "slug" existe en la base de datos
    if Producto.objects.filter(activo=True, slug=slug).exists():
        template_name   = 'core/WEB/Productos/detail.html'
        # variable que guarda el objeto de tipo producto en el caso de que sea un producto activo y que tenga el nombre enviado desde el front por "slug" 
        # esta variable se enviara como contexto al front dentro de una lista.
        producto        = Producto.objects.get(activo=True, slug=slug)        
        context         = {"producto":producto}
        return render(request, template_name, context)
#Método que agregará los productos seleccionados en el carrito de compra
def cart(request,slug):
    # variable que guarda el objeto de tipo producto en el caso de que tenga el nombre enviado desde el front por "slug" 
    product     = Producto.objects.get(slug=slug)
    #variable que guarda un diccionario con distintos tipos de variables inicializadas, estos serviran para guardar los productos enviados desde el front
    initial     = {"items":[], "price": 0, "count": 0}
    # variable que guarda la session actual y la une al diccicionario creado en el paso anterior y guardado en la variable "initial"
    session     = request.session.get("data", initial)

    if slug in session["items"]: # esta validación restringirá los items a solo 1 por carro
        messages.error(request,"Producto ya existe en el Carrito")
    else:
        session["items"].append(slug)
        session["price"] += product.precioProducto
        session["count"] += 1
        request.session["data"] = session
        messages.success(request, "Agregado Exitosamente.")
        #redireccionamento al detalle del producto agregado
    return redirect("core:detail", slug)

#Método para eliminar objetos del carrito (no funcional aun)
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

#Método para visualizar el carrito de compra
def mycart(request):
    template_name    = 'core/WEB/Productos/carritoCompras.html'
    # variable que guarda el diccionario de la data de la sesion
    sess             = request.session.get("data", {"items":[]})
    # variable que guarda los objetos de tipo producto filtrados por si estan activos y los "slug" estan dentro de la lista guardada en la variable sess
    products         = Producto.objects.filter(activo=True, slug__in = sess["items"])
    # variable que guarda una lista que contiene los productos guardados en la variable "products"
    context          = {"productos":products}
    return render(request, template_name, context)