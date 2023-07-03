from django.urls import path
from rest_producto.views import lista_productos, detalle_producto, lista_categorias, detalle_categoria, lista_usuarios, detalle_usuario, lista_listasCompra, detalle_listaCompra
from .viewslogin import login

urlpatterns = [
    path('lista_productos', lista_productos, name='lista_productos'),
    path('detalle_producto/<id>', detalle_producto, name='detalle_producto'),
    
    path('lista_categorias', lista_categorias, name='lista_categorias'),
    path('detalle_categoria/<id>', detalle_categoria, name='detalle_categoria'),

    path('lista_usuarios', lista_usuarios, name='lista_usuarios'),
    path('detalle_usuario/<id>', detalle_usuario, name='detalle_usuario'),

    path('lista_listasUsuario', lista_listasCompra, name='lista_listasUsuario'),
    path('detalle_listaUsuario/<id>', detalle_listaCompra, name='detalle_listaUsuario'),

    path('login', login, name="login"),
]