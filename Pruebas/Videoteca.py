### Programa que simula una tienda de alquilamiento de películas.
### El programa tiene dos modos de funcionamiento: Administrador y usuario que alquia la película.
### En el modo Adminitración se pueden agregar/eliminar/modificar peliculas y usuarios. 
### En el modo de usuario se pueden alquilar películas y devolver películas, y ha de tener en cuenta que se pasan mas de 48 horas se aplique el recargo.
### Recargo de 10€ por día de retraso, una ver pasado 48 horas.
### Se guarda el inventario de Peliculas y Usuarios en disco com módulo json.
from datetime import datetime, timedelta
from datetime import time
from SupermercadoV2 import producto
import json

class pelicula:
    id : int
    nombre : str
    precio : float
    fecha_alquiler = '' 
    fecha_devolucion = ''
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio
    def __str__(self):
        return f"{self.nombre} - {self.precio}€"
    def cantidad(self, cantidad):
        self.cantidad = cantidad
    def calc_recargo(self):
        if self.fecha_devolucion == '' or self.fecha_alquiler == '':
            return 0
        date1 = time.strptime(self.fecha_alquiler, "%d/%m/%Y")
        date2 = time.strptime(self.fecha_devolucion, "%d/%m/%Y")
        if date1 + timedelta(days=2) < date2:
            return (date2 - date1 - timedelta(days=2)).days * 10
    def esta_libre(self):
        if self.fecha_alquiler == '' or time.strptime(self.fecha_devolucion, "%d/%m/%Y") < datetime.now():
            return True
        else:
            return False
class    usuario:
    id : int
    nombre : str
    password: str
    peliculas_alquiladas = []
    def __init__(self, id, nombre, password):
        self.id = id
        self.nombre = nombre
        self.password = password
    def __str__(self):
        return f"{self.nombre}"
    def alquilar(self, pelicula_id, fecha_alquiler):
        # Buscar Objeto pelicula por id, añadir objeto a la lsita de peliculas alquiladas y actualizar en el objeto la fecha de alquiler
        pass
    def devolver(self, pelicula_id, fecha_devolución):
        # Buscar Objeto pelicula por id, eliminar objeto en la lsita de peliculas alquiladas y actualizar en el objeto la fecha de devolución
        pass


class menu:
    def menu_inicial(self):
        print('---------------------------------')
        print('Introduce usuario: ')
        print('---------------------------------')
        user = input()
        print('Introduce contraseña: ')
        password = input()
        if user == 'admin' and password == 'admin':
            self.admin = usuario(0, 'admin', 'admin')
            self.menu_admin()
        else:
            self.user = usuario(1, user, password)
            self.menu_usuario()
    def menu_admin(self):
        while True:
            print('---------------------------------')
            print('Menú Administrador')
            print('---------------------------------')
            print('1. Añadir película')
            print('2. Eliminar película')
            print('3. Modificar película')
            print('4. Listar películas')
            print('5. Salir')
            print('---------------------------------')
            opcion = input()
            if opcion == '1':
                self.add_pelicula()
            elif opcion == '2':
                self.del_pelicula()
            elif opcion == '3':
                self.mod_pelicula()
            elif opcion == '4':
                self.list_peliculas()
            else:
                break
    def menu_usuario(self):
        self.load_users()
        self.load_peliculas()
        while True:
            print('---------------------------------')
            print('Menú Usuario')
            print('---------------------------------')
            print('1. Alquilar película')
            print('2. Devolver película')
            print('3. Salir')
            print('---------------------------------')
            opcion = input()
            if opcion == '1':
                self.alquilar_pelicula()
            elif opcion == '2':
                self.devolver_pelicula()
            else:
                break
    def load_users(self):
        pass
    def add_pelicula(self):
        pass
    def del_pelicula(self):
        pass
    def mod_pelicula(self):
        pass
    def list_peliculas(self):
        pass
    def load_peliculas(self):
        pass
    def alquilar_pelicula(self):
        pass
    def devolver_pelicula(self):
        pass



        

if __name__ == '__main__':
    m = menu()
    m.menu_inicial()






