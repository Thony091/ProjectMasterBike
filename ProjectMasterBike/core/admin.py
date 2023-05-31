from django.contrib import admin
from .models import Categoria, Region, Comuna, Usuario, Producto, ListaCompras
# Register your models here.

admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(ListaCompras)


