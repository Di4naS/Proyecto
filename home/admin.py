from django.contrib import admin
from .models import Marca, Categoria, Producto, Perfil

# Register your models here.
admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Perfil)
