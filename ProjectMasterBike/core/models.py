from django.db import models
from django.contrib.auth.models import AbstractUser
from autoslug import AutoSlugField

# Create your models here.

class Region(models.Model):
    idRegion                = models.AutoField(primary_key = True, verbose_name = 'Id de categoria')
    nombreRegion            = models.CharField(max_length = 30, verbose_name = 'Nombre de region')

    def __str__(self):
        return self.nombreRegion

class Comuna(models.Model):
    idComuna                = models.AutoField(primary_key = True, verbose_name = 'Id de comuna')
    nombreComuna            = models.CharField(max_length = 70, verbose_name = 'Nombre de comuan')
    region                  = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreComuna

class Usuario(models.Model):
    idUsuario               = models.AutoField(primary_key = True, verbose_name = 'Id de usuario')
    nombreUsuario           = models.CharField(max_length = 70, verbose_name = 'Nombre del usuario')
    apellidoUsuario         = models.CharField(max_length = 70, verbose_name = 'Apellido del usuario')
    rutUsuario              = models.CharField(max_length = 70, verbose_name = 'Rut del usuario')
    emailUsuario            = models.EmailField(max_length = 30, unique = True, verbose_name = 'Email del usuario')
    contraseniaUsuario      = models.CharField(max_length = 30, verbose_name = 'Contraseña del usuario')
    direccionUsuario        = models.CharField(max_length = 70, null = True, verbose_name='Dirección del usuario')
    comuna                  = models.ForeignKey(Comuna, null=True, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombreUsuario

class Categoria(models.Model):
    idCategoria             = models.AutoField(primary_key = True, verbose_name='Id de categoria')
    nombreCategoria         = models.CharField(max_length = 30, verbose_name='Nombre de categoria')
    slug                    = AutoSlugField(populate_from="nombreCategoria", null=True)
    activo                  = models.BooleanField(default="True")
    
    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    idProducto              = models.AutoField(primary_key = True, verbose_name = 'Id de producto')
    nombreProducto          = models.CharField(max_length = 50, verbose_name = 'Nombre del producto')
    slug                    = AutoSlugField(populate_from="nombreProducto", null=True)
    imagen                  = models.CharField(max_length=250, null=True )    
    caracteristicaProducto  = models.CharField(max_length = 255, verbose_name='Descripcion del producto')
    precioProducto          = models.IntegerField(verbose_name='Precio de producto')
    stock                   = models.PositiveIntegerField("Cantidad del producto en stock", default=0)
    categoria               = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    destacado               = models.BooleanField(default="True")
    activo                  = models.BooleanField(default="True")

    def __str__(self):
        return self.nombreProducto

class ListaCompras(models.Model):
    idListaCompras          = models.AutoField(primary_key = True, verbose_name='Id de la lista de compras')
    valorTotalCompra        = models.IntegerField(null = True, blank = True, verbose_name='Valor total de compra')
    cantidadProductos       = models.IntegerField(null = True, blank = True, verbose_name = 'Cantidad de productos')
    producto                = models.ForeignKey(Producto, on_delete = models.CASCADE)
    usuario                 = models.ForeignKey(Usuario, on_delete = models.CASCADE)

    def __str__(self):
        return self.valorTotalCompra
