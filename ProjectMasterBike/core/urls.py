from django.urls import path, include
from .views import index, historia, metodos_envio, nuestras_tiendas, preguntas_frecuentes, ayuda_contrasenia, user_login, pedidos, usuario, registro_bike, registro_usuario, seguimiento_envio, productos_servicios, contactanos,  servicios, buscar_categorias,  detail, cart, mycart, signout, eliminar_producto

app_name='core'

urlpatterns = [
    path('', index, name="index"),
    path('historia', historia, name="historia"),
    path('metodos_envio', metodos_envio, name="metodos_envio"),
    path('nuestras_tiendas', nuestras_tiendas, name="nuestras_tiendas"),
    path('preguntas_frecuentes', preguntas_frecuentes, name="preguntas_frecuentes"),
    path('ayuda_contrasenia', ayuda_contrasenia, name="ayuda_contrasenia"),
    path('login', user_login, name="login"),
    path('pedidos', pedidos, name="pedidos"),
    path('principalUsuario', usuario, name="principalUsuario"),
    path('registro_bike', registro_bike, name="registro_bike"),
    path('registro_usuario', registro_usuario, name="registro_usuario"),
    
    path('seguimiento_envio', seguimiento_envio, name="seguimiento_envio"),
    path('contactanos', contactanos, name="contactanos"),
    path('productosYservicios', productos_servicios, name="productosYservicios"),
    path('servicios', servicios, name="servicios"),

    path('detail/<slug>', detail, name='detail'),
    path('eliminar/<slug>', eliminar_producto, name='eliminar_producto'),
    path('<slug>/cart', cart, name='cart'),
    path('mycart/', mycart, name='mycart'),
    path('categorias/<slug>', buscar_categorias, name="categorias"),


    path('logout/', signout, name="logout")

]