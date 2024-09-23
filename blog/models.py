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
    
class Post(models.Model):
    Titulo=models.CharField(max_length=90)
    Contenido=models.CharField(max_length=255)
    Imagen=models.ImageField(upload_to='blog', null=True, blank=True)
    Created=models.DateTimeField(auto_now_add=True)
    Updated=models.DateTimeField(auto_now_add=True)
    Autor=models.ForeignKey(User, on_delete=models.CASCADE)
    Categorias=models.ManyToManyField(Categoria)

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'

    def __str__(self):
        return self.Titulo 