from Clase_Productos import Producto
from Clase_Usuario import Usuario
from Clase_Carrito import Carrito
from Clase_Gestion_Ficheros import ficheros
import time
import os

### Tienda CLI
### Esta tienda mantiene dos ficheros para los productos y para los usuarios, la clase carrito va en memoria.
### Los ficheros de los productos y usuarios se guardan en formato json.
### Una vez se finalice un pedido, se creará un ficheros con los datos del pedido a modo de historico.
### Existirán dos menus, uno para los administradores que dan de alta usuarios y productos.
## El segundo menú es para los usuarios que pueden ver los productos disponibles y hacer pedidos.

def menu_inicial():
    """Python DocString: Funcion inicial que permite el acceso al sistema como Administrado o como consumidor"""
    fich = ficheros()
    users = []
    rol = ''
    os.system("clear")
    print("*" * 150)
    print("*" * 150)
    print("Bienvenido al programa Tienda CLI, debes ingresar usuario y password para acceder.")
    print("*" * 150)
    print("*" * 150)
    user = input('Introduce Nickname: ')
    pwd = input('Introduce Password: ')
    if user == 'admin' and pwd =='nimda':
        menu_admin()
    else:
        menu_user()
#        users = fich.carga_usuarios()
#        for u in users:
#            if u.check_user(user, pwd):
#                if u.check_role():
#                    menu_admin()
#                else:
#                    menu_user()
#        print("Lo sentimos, no hemos encontrado el usuario en nuetra Base de Datos.")

def menu_admin():
    '''Función para lanzar menu para gestión usuarios y productos'''
    os.system("clear")
    print("*" * 150)
    print("*" * 150)
    print("Bienvenido al menú de Administración:")
    print("Elija una de las siguientes opciones:")
    print("*" * 150)
    print("1 - Añadir Usuario")
    print("2 - Añadir Producto")
    print("3 - Salir")
    opt = input("Elección: ")
    if opt == "1":
        add_user()
    elif opt == "2":
        add_product()
    else:
        print("Adiós.")

def add_user():
    print("*" * 150)
    id = int(input("Introduce ID: "))
    nombre = input("Introduce Nombre: ")
    nick = input("Introduce Nick: ")
    password = input("Introduce Password: ")
    role_admin = input("Introduce rol (0-> Usuario, 1-> Administrador): ")
    usertemp = Usuario(id, nombre, nick, password, role_admin==1)
    filetemp = ficheros()
    filetemp.gravar_usuario(usertemp)
    print("Usuario Registrado.")
    time.sleep(5)
    exit()

def add_product():
    print("*" * 150)
    id = int(input("Introduce ID: "))
    nombre = input("Introduce Nombre Producto: ")
    descr = input("Introduce Descripción del Producto: ")
    precio = float(input("Introduce Precio: "))
    productempt = Producto(id,nombre,descr,precio)
    filetemp = ficheros()
    filetemp.gravar_producto(productempt)
    print("Producto Registrado.")
    time.sleep(5)
    exit()

def menu_user():
    '''Funcion para mostrar menu usuario para ver productos, añadir al carrito y finalizar compra'''
    pass


if __name__ == '__main__':
    menu_inicial()
    