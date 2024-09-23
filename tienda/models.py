from django.db import models
from django. contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    Nombre=models.CharField(max_length=80)
    Created=models.DateTimeField(auto_now_add=True)
    Updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.Nombre 
    
class Producto(models.Model):
    Nombre=models.CharField(max_length=90)
    Contenido=models.CharField(max_length=255)
    Imagen=models.ImageField(upload_to='tienda', null=True, blank=True)
    Precio=models.FloatField()
    Disponibilidad=models.BooleanField(default=True)
    Categorias=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    Created=models.DateTimeField(auto_now_add=True)
    Updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'

    def __str__(self):
        return self.Nombre