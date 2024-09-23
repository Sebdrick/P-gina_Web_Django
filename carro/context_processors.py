def importe_total(request):
    total = 0
    if request.user.is_authenticated and "carro" in request.session:                    
        for key, value in request.session["carro"].items():
            total = total + float(value["Precio"]) * value["Cantidad"]
    return {"importe_total": total}