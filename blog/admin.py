from django.contrib import admin
from .models import Categoria
from .models import Post

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('Created','Updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('Created','Updated')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)