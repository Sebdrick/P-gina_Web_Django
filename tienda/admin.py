from django.contrib import admin
from .models import Categoria
from .models import Producto

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('Created','Updated')

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=('Created','Updated')

admin.site.register(Categoria, CategoriaAdmin)    
admin.site.register(Producto, ProductoAdmin)