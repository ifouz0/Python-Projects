from Clase_Productos import Producto
from Clase_Usuario import Usuario
from Clase_Carrito import Carrito
from Clase_Gestion_Ficheros import ficheros
from Clase_Menus import Menu

### Tienda CLI
### Esta tienda mantiene dos ficheros para los productos y para los usuarios, la clase carrito va en memoria.
### Los ficheros de los productos y usuarios se guardan en formato json.
### Una vez se finalice un pedido, se creará un ficheros con los datos del pedido a modo de historico.
### Existirán dos menus, uno para los administradores que dan de alta usuarios y productos.
## El segundo menú es para los usuarios que pueden ver los productos disponibles y hacer pedidos.



if __name__ == '__main__':
    m = menu()
    m.menu_inicial()