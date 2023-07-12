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
    else: #al ser "else" se entiende que el 'method="post"'
        #Autenticamos el usuario y el password con el método "Authenticate"(método de django) y lo guardamos en una variable
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None: #pregunta si el usuario no se encontro en bd reenvia el formularia y un mensaje de error.             
            return render(request, template_name,{'form': AuthenticationForm,
                        'error': 'usuario no encontrado'})
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
    # variable que guarda la "forma" para la creacion de un usuario, se podrá renderizar cuando se invoque la url asociada a este método
    data = {
        'form': ClienteCreationForm()
    }

    if request.method == 'POST':
        # variable que guarda la data enviada desde el front con el "method='post'" 
        user_creation_form = ClienteCreationForm(data=request.POST)
        # se pregunta si el formulario creado anteriormente es valido(is_valid) se podran seguir los pases dentro de este "if"
        if user_creation_form.is_valid():
            try:#capturamos posibles errores con un try-except
                user_creation_form.save()#Si estamos en este punto es porque se confirmo la validacion y se guardara en la base de datos(.save)
                messages.success(request, "Usuario Registrado.")#se envia un mensaje al front con el metodo "messages"
                user = authenticate(username=user_creation_form.cleaned_data['username'],password=user_creation_form.cleaned_data['password1'])
                #Variable que guarda el resultado de la autentificación efectuada con el método "authenticate" método propio del django, este método
                #toma el username y el password recientemente creado y los compara con los de la base de datos para autentificarlos.
                login(request, user)#Este método propio de django logea el usuario autentificado en el paso anterior
                return redirect('core:index')#Se indica  la redirección a la pagina deseada
            except IntegrityError:#En el caso de un error de base de datos, entrará en este apartado
                #Se retorna a la misma página con el formulario y un mensaje de error, estos ultimos tienen que ser invocados en el front 
                # por el desarrollador
                return render(request, template_name, {"form": ClienteCreationForm, "error": "Usuario ya existe."})
        else:#De no validarse la info del formulario se llega a este apartado  que guarda el formulario vacio en una variable y la envia nuevamente
             #a la página para ser invocado en el front por el desarrollador
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
#Método que renderiza una página al ser llamado
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
    productos       = Producto.objects.filter(activo=True, categoria = cat)
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
    #Variable que guarda el objeto de tipo producto en el caso de que tenga el nombre enviado desde el front por "slug" 
    product     = Producto.objects.get(slug=slug)
    #Variable que guarda un diccionario con distintos tipos de variables inicializadas, estos serviran para guardar los productos enviados desd el front
    initial     = {"items":[], "price": 0, "count": 0}
    #Variable que guarda la session actual y la une al diccicionario creado en el paso anterior y guardado en la variable "initial"
    session     = request.session.get("data", initial)

    if slug in session["items"]:# esta validación restringirá los items a solo 1 por carro y enviará un mensaje al front
        messages.error(request,"Producto ya existe en el Carrito")
    else:
        session["items"].append(slug)#Agregamos a la lista de "items" de la variable sesion, un nuevo item con el nombre enviad desd el front con "slug"
        session["price"] += product.precioProducto #Sumamos a la lista de precio(price) el precio del producto enviado desde el front
        session["count"] += 1 #Sumamos a la lista contadora(count) 1 (+=) cada vez que se agrega un nuevo producto desde el front
        request.session["data"] = session
        #Reemplazamos la data de la session actual con la variable session creada anteriormente y poblada con las iteracciones de la persona en la web.
        messages.success(request, "Agregado Exitosamente.")#Mensaje que podra ser utilizado en el front
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