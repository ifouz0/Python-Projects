from Clase_Historia import Historia

### Tienda CLI
### Esta tienda mantiene dos ficheros para los productos y para los usuarios, la clase carrito va en memoria.
### Los ficheros de los productos y usuarios se guardan en formato json.
### Una vez se finalice un pedido, se creará un ficheros con los datos del pedido a modo de historico.
### Existirán dos menus, uno para los administradores que dan de alta usuarios y productos.
## El segundo menú es para los usuarios que pueden ver los productos disponibles y hacer pedidos.



if __name__ == '__main__':
    name = input("Introduce tu nombre: ")
    print(f"Bienvenido {name} a la historia interactiva. Eres un aventurero en busqueda de tesoros.")
    historia = Historia()
    fin = False
    while not fin:
        fin = historia.mostrar()
        if fin:
            print("Gracias por jugar.")
            break
        opcion = int(input("Introduce la opción que deseas realizar: "))
        historia.elegir_opcion(opcion) 


