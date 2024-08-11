from datetime import datetime
from Clase_Productos import Producto
from Clase_Usuario import Usuario


class Carrito:
    user: Usuario
    productos = [] 
    fecha_compra = ''
    def __init__(self, user: Usuario):
        self.user = user
    def añadirProducto(self, product: Producto):
        self.productos.append(product)
    def eliminarProducto(self, product_id: int) -> bool:
        result = False
        for p in self.productos:
            if p == product_id:
                self.productos.remove(p)
                return True
    def descuento(self, descuento: float):
        for p in self.productos:
            p.descuento(descuento)
    def finalizarCompra(self) -> float:
        self.fecha_compra = datetime.now()
        total = 0.0
        for p in self.productos:
            totalº += p.precio()
        return total