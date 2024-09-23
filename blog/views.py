from django.shortcuts import render
from blog.models import Post
from blog.models import Categoria

# Create your views here. 

def blog(request):
    posts = Post.objects.all()
    categorias = Categoria.objects.all().distinct()
    return render(request, "blog/blog.html", {"posts": posts, "categorias": categorias}) 

def categoria(request, categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(Categorias=categoria)
    return render(request, "blog/categorias.html", {"categoria": categoria, "posts": posts})           