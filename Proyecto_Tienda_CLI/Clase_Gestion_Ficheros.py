import json
from Clase_Productos import Producto
from Clase_Usuario import Usuario
from Clase_Carrito import
### Clase para la gestión de los ficheros en donde se guardan los productos, usuarios y pedidos, cada uno en un fichero aparte.

class ficheros:
    path: str = "C:\Users\A200324620\OneDrive - Deutsche Telekom AG\Dokumente\VSCode\Proyecto Tienda CLI"
    file_user: str = "usuarios.json"
    file_product: str = "productos.json"
    file_pedidos: str = "pedidos.json"
    def __init__(self):
        self.path = self.path + "\\"
        self.file_user = self.path + self.file_user
        self.file_product = self.path + self.file_product
        self.file_pedidos = self.path + self.file_pedidos
    def carga_usuarios(self):
        usuarios = []
        try:
            with open(self.file_user, "r") as file:
                data = json.load(file)
                for item in data:
                    usuarios.append(Usuario(item["id"], item["nombre"], item["password"]))
        except:
            usuarios = []
            print("Error al cargar los usuarios, se genera fichero vacio.")
            with open(self.file_user, "w") as file:
                json.dump(usuarios, file)
        return usuarios
    def carga_productos(self):
        productos = []
        try:
            with open(self.file_product, "r") as file:
                data = json.load(file)
                for item in data:
                    productos.append(Producto(item["id"], item["nombre"], item["descripcion"], item["precio"]))
        except:
            productos = []
            print("Error al cargar los productos, se genera fichero vacio.")
            with open(self.file_product, "w") as file:
                json.dump(productos, file)
        return productos
    def gravar_usuario(self, usuario):
        usuarios = self.carga_usuarios()
        usuarios.append(usuario)    
        with open(self.file_user, "w") as file:
            json.dump(usuarios, file, default=lambda x: x.__dict__)
    def gravar_producto(self, producto):
        productos = self.carga_productos()
        productos.append(producto)
        with open(self.file_product, "w") as file:
            json.dump(productos, file, default=lambda x: x.__dict__)
    def eliminar_producto(self, producto):
        productos = self.carga_productos()
        productos.remove(producto)
        with open(self.file_product, "w") as file:
            json.dump(productos, file, default=lambda x: x.__dict__)
    def eliminar_usuario(self, usuario):
        usuarios = self.carga_usuarios()
        usuarios.remove(usuario)
        with open(self.file_user, "w") as file:
            json.dump(usuarios, file, default=lambda x: x.__dict__)