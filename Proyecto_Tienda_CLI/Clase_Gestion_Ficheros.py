import csv
from Clase_Productos import Producto
from Clase_Usuario import Usuario
from Clase_Carrito import Carrito
### Clase para la gestión de los ficheros en donde se guardan los productos, usuarios y pedidos, cada uno en un fichero aparte.

class ficheros:
    path: str = "/Users/ivanfouzrodriguez/VSCode/Python-Projects/Proyecto_Tienda_CLI/"
    file_user: str = "usuarios.csv"
    file_product: str = "productos.csv"
    file_pedidos: str = "pedidos.csv"
    usuarios = []
    productos =[]

    def __init__(self):
        self.file_user = self.path + self.file_user
        self.file_product = self.path + self.file_product
        self.file_pedidos = self.path + self.file_pedidos
        self.usuarios = self.carga_usuarios()
        self.productos = self.carga_productos()

    @classmethod
    def carga_usuarios(cls):
        try:
            with open(cls.file_user, newline='') as file:
                data = csv.DictReader(file)
                for item in data:
                    cls.usuarios.append(Usuario(item["id"], item["nombre"], item["nick"], item["password"], item["role_admin"]))
        except:
            tmp_user = Usuario(0,'admin','admin','nimda',1)
            print("Error al cargar los usuarios, se genera fichero vacio.")
            file.close()
            with open(cls.file_user, newline='') as file:
                fieldnames= ["id", "nombre", "nick", "Password", "role_admin"]
                writer =csv.DictWriter(file,fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow('id': 0, "nombre": "admin", "nick": "admin", "role_admin": True)
                file.close()
        return cls.usuarios
    
    @classmethod
    def carga_productos(cls):
        try:
            with open(cls.file_product, "r") as file:
                data = json.load(file)
                for item in data:
                    cls.productos.append(Producto(item["id"], item["nombre"], item["descripcion"], item["precio"]))
        except:
            print("Error al cargar los productos, se genera fichero vacio.")
            with open(cls.file_product, "w") as file:
                json.dump(cls.productos, file)
        return cls.productos
    
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
