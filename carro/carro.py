class Carro:

    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            self.carro = self.session["carro"] = {}
        else:
            self.carro = carro


    def agregar(self, producto):
        if str(producto.id) not in self.carro.keys():
            self.carro[producto.id] = {
                "Producto_id": producto.id,
                "Nombre": producto.Nombre,
                "Precio": float(producto.Precio),  
                "Cantidad": 1,
                "Imagen": producto.Imagen.url,
            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["Cantidad"] += 1
                    break
        self.guardar_carro()


    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True


    def eliminar(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()


    def restar(self, producto):
        for key, value in self.carro.items():
            if key == str(producto.id):
                value["Cantidad"] -= 1
                if value["Cantidad"] < 1:
                    self.eliminar(producto)
                break
        self.guardar_carro()


    def limpiar(self):
        self.session["carro"] = {}
        self.session.modified = True