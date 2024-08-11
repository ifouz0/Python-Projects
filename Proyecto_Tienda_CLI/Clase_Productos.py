### Clase Producto con los siguientes atributos:
### id: int
### nombre: str
### descripcion: str
### precio: float


class Producto:
    id: int
    nombre: str
    descripcion: str
    precio: float
    def __init__(self, id, nombre, descripcion, precio) -> None:
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
    def __str__(self):
        return f"{self.nombre} - {self.precio}€"
    def cargo(self, procentage):
        self.precio += self.precio * (procentage / 100)
        return self.precio
    def descuento(self, procentage):
        self.precio -= self.precio * (procentage / 100)
        return self.precio
    def __eq__(self, other):
        return self.id == other.id
    def modificar(self, nombre, descripcion, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        return self
    def precio(self) -> float:
        return self.precio
