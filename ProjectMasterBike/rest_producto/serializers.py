from rest_framework import serializers
from core.models import Producto, Usuario, Categoria, ListaCompras

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = [
            'idProducto',
            'nombreProducto',
            'slug',
            'imagen',
            'caracteristicaProducto',
            'precioProducto',
            'stock',
            'categoria',
            'destacado',
            'activo'
            ]

# Compartiendo espacio xD
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'idUsuario',
            'nombreUsuario',
            'apellidoUsuario',
            'rutUsuario',
            'emailUsuario',
            'contraseniaUsuario',
            'direccionUsuario',
            'comuna'
        ]
        
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = [
            'idCategoria',
            'nombreCategoria',
            'slug',
            'activo'
        ]

class ListaComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaCompras
        fields = [
            'idListaCompras',
            'valorTotalCompra',
            'cantidadProductos',
            'producto',
            'usuario'
        ]