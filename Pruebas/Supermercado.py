class producto:
    id : int
    nombre : str
    precio : float
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Precio: {self.precio}"
    def __repr__(self):
        return str(self)
    def __eq__(self, other):
        return self.id == other.id
    def __ne__(self, other):
        return not self.__eq__(other)
    def __lt__(self, other):
        return self.precio < other.precio
    def __le__(self, other):
        return self.precio <= other.precio
    def __gt__(self, other):
        return self.precio > other.precio
    def __ge__(self, other):
        return self.precio >= other.precio
    def cargo (self, procentage):
        self.precio += self.precio * ( procentage/ 100 )
        return self.precio
    def descuento(self, procentage):
        self.precio -= self.precio * ( procentage/ 100 )
        return self.precio

class usuario:
    id : int
    nombre : str
    def __init__(self):
        #self.id = id
        #self.nombre = nombre
        pass
#    def __str__(self):
#        return f"ID: {self.id}, Nombre: {self.nombre}"
#    def __repr__(self):
#        return str(self)
    def __eq__(self, other):
        return self.id == other.id
    def __ne__(self, other):
        return not self.__eq__(other)
    def carga_user(self):
        print("")
        print("Bienvenido al Supermercado")
        print("")
        print("Por favor ingrese su nombre:")
        nombre = input()
        self.nombre = nombre
        print("Por favor ingrese su id:")
        id = input()
        self.id = id
    def print_id(self):
        return self.id
    def print_nombre(self):
        return self.nombre
        

class carrito:
    id : int
    usuario = usuario()
    productos : list
    def __init__(self, id, usuario):
        self.id = id
        self.usuario = usuario
        self.productos = []
    def agregar(self, producto):
        self.productos.append(producto)
    def eliminar(self, producto):
        self.productos.remove(producto)
    def total(self):
        total = 0
        for p in self.productos:
            total += p.precio
        return total
    def lista_productos(self):
        lista_p = {}
        for p in self.productos:
            lista_p[p.nombre] = p.precio
        return lista_p
    def menu(self):
        while True:
            print("Menu")
            print("1. Agregar Producto")
            print("2. Eliminar Producto")
            print("3. Calcular Total")
            print("4. Listar Productos")
            print("5. Salir")
            print("6. Aplicar Descuento")
            print("Seleccione una opción:")
            opcion = input()
            if opcion == "1":
                print("Agregar Producto")
                print("Ingrese el ID del producto:")
                id = int(input())
                print("Ingrese el nombre del producto:")
                nombre = input()
                print("Ingrese el precio del producto:")
                precio = float(input())
                self.agregar(producto(id, nombre, precio))
                self.menu()
            elif opcion == "2":
                print("Eliminar Producto")
                print("Ingrese el ID del producto:")
                id = int(input())
                self.eliminar(producto(id, nombre, precio))
                self.menu()
            elif opcion == "3":
                print("Total")
                print(f"El total de la compra es: {self.total()}")
                self.menu()
            elif opcion == "4":
                print("Listar Productos")
                print(self.lista_productos())
                self.menu()
            elif opcion == "5":
                print("Salir")
                break
            elif opcion == "6":
                print("Aplicar Descuento")
                print("Ingrese el porcentaje de descuento:")
                descuento = int(input())
                for p in self.productos:
                    p.descuento(descuento)
                print("Descuento aplicado")
                self.menu()
            else:
                print("Opción no válida")
                self.menu()


    



if __name__ == "__main__":
    #Identificar Usuario
    user1 = usuario()
    user1.carga_user()
    carrito1 = carrito(user1.print_id, user1.print_nombre)
    carrito1.menu()






    

