from django.shortcuts import render
from .models import Producto

# Create your views here.

def tienda(request):
    if "carro" not in request.session:
        request.session["carro"] = {}
    productos=Producto.objects.all()
    return render(request, "tienda/tienda.html", {"productos":productos})            