from Clases import *

class Menu:
    usuario : str
    escuela : Escuela

    def __init__(self, usuario):
        self.usuario = usuario
        self.escuela = None
    
    def menu_principal(self):
        print('')
        print('')
        print('')
        print('-'*50)
        print(f'Bienvenido {self.usuario}')
        print('En este proyecto vamos a simular un sistema de escuela con sus aulas y alumnos, y vamos a guardar los datos en un archivo CSV de forma automática y sin que requiera tu atención.')
        print ('')
        print(' Menú Principal:')
        print('Estas son las opciones principales que puedes escoger:')
        if self.escuela is None:
            print('1. Insertar los datos de la escuela')
        else:
            print('1. Modificar los datos de la escuela')
            print('2. Ver datos de la escuela y Aulas')
            print('3. Crear una Aula')
            if self.escuela.existen_aulas() == True:
                print('4. Crear un Alumno')
                print ('5. Listar ocupación de aulas')
                print ('6. Listar profesores y número de alumnos')
                if self.escuela.existen_alumnos() == True:
                    print('7. Listar Alumnos')
                    print ('8. Listar Alumnos aprobados')
                    print ('9. Listar Alumnos mayores de edad')
                    print ('10. Calificar Alumnos de un Aula')
        print('11. Salir')
        print ('')
        print('-'*50)
        opcion = input('Seleccione una opcion: ')
        if opcion == '1':
            self.modificar_datos_escuela()
            return False
        elif opcion == '2':
            if self.escuela is not None:
                self.ver_datos_escuela()
            else:
                print('Primero debes insertar los datos de la escuela')
            return False
        elif opcion == '3':
            if self.escuela is not None:
                self.crear_aula()
            else:
                print('Primero debes insertar los datos de la escuela')
            return False
        elif opcion == '4':
            if self.escuela.existen_aulas() == True:
                self.crear_alumno()
            else:
                print('Primero debes crear un aula')
            return False
        elif opcion == '5':
            if self.escuela.existen_aulas() == True:
                self.listar_ocupacion()
            else:
                print('No existen aulas')
            return False
        elif opcion == '6':
            if self.escuela.existen_aulas() == True:
                self.listar_profesores_num_alumnos()
            else:
                print('No existen aulas')
            return False
        elif opcion == '7':
            if self.escuela.existen_alumnos() == True:
                self.listar_alumnos()
            else:
                print('No existen alumnos')
            return False
        elif opcion == '8':
            if self.escuela.existen_alumnos() == True:
                self.listar_aprobados()
            else:
                print('No existen alumnos')
            return False
        elif opcion == '9':
            if self.escuela.existen_alumnos() == True:
                self.listar_alumnos_mayores_edad()
            else:
                print('No existen alumnos')
            return False
        elif opcion == '10':
            if self.escuela.existen_alumnos() == True:
                self.calificar_alumnos()
            else:
                print('No existen alumnos')
            return False
        elif opcion == '11':
            print('Gracias por participar, hasta luego')
            return True
        else:
            print('Opción no válida')
            o = input ('Quieres salir (S/N)?').upper()
            return True if o == 'S' else False
    
    def modificar_datos_escuela(self):
        if self.escuela is None:
            print ('')
            print ('*'*50)
            print ('Creación de la Escuela:')
            nombre = input('Nombre de la escuela: ')
            direccion = input('Dirección de la escuela: ')
            telefono = input('Teléfono de la escuela: ')
            director = input('Nombre del director: ')
            self.escuela = Escuela(nombre, direccion, telefono, director)
            print(f'Escuela {nombre} creada correctamente')
        else:
            print ('')
            print ('*'*50)
            print ('Modificación de la Escuela:')
            nombre = input('Nombre de la escuela: ')
            direccion = input('Dirección de la escuela: ')
            telefono = input('Teléfono de la escuela: ')
            director = input('Nombre del director: ')
            self.escuela.nombre = nombre
            self.escuela.direccion = direccion
            self.escuela.telefono = telefono
            self.escuela.director = director
            print(f'Escuela {nombre} modificada correctamente')
        
        opcion = input('Quieres agregar aulas a la escuela (S/N)?').upper()
        if opcion == 'S':
            self.crear_aula()
        else:
            return False

    def ver_datos_escuela(self):
        print ('')
        print ('*'*50)
        print ('Datos de la Escuela:')
        self.escuela.listar_datos_escuela()
        return False

    def crear_aula(self):
        print ('')
        print ('*'*50)
        print ('Creación de Aula:')
        nombre = input('Nombre del aula: ')
        capacidad = int(input('Capacidad del aula: '))
        profesor = input('Nombre del profesor: ')
        self.escuela.agregar_aula(Aula(nombre, capacidad, profesor))
        print(f'Aula {nombre} creada correctamente')
        opcion = input ('Quieres crear alumnos para esta aula (S/N)?').upper
        if opcion == 'S':
            self.crear_alumno(nombre_aula=nombre)
        else:
            return False

    def crear_alumno(self, nombre_aula = None):
        print ('')
        print ('*'*50)
        print ('Creación de Alumno:')
        nombre = input('Nombre del alumno: ')
        edad = int(input('Edad del alumno: '))
        if nombre_aula is None:
            print('Aulas disponibles:')
            print ('')
            for aula in self.escuela.aulas:
                if aula.ocupacion() < 100:
                    print(aula.nombre)
            aula_name = input('Nombre del aula: ')
            print ('')
        else:
            aula_name = nombre_aula
        encontrado = False
        for aula in self.escuela.aulas:
            if aula.nombre == aula_name:
                aula.agregar_alumno(Alumno(nombre, edad))
                print(f'Alumno {nombre} creado correctamente en el aula {aula_name}')
                encontrado = True
                return False
        if encontrado == False:
            print(f'Aula {aula_name} no encontrada. Alumno no creado')
            return False

    def listar_ocupacion(self):
        print ('')
        print ('*'*50)
        print ('Ocupación de Aulas:')
        self.escuela.listar_ocupacion()
        return False
    
    def listar_profesores_num_alumnos(self):
        print ('')
        print ('*'*50)
        print ('Profesores y número de alumnos:')
        self.escuela.listar_profesores_num_alumnos()
        return False
    
    def listar_alumnos(self):
        print ('')
        print ('*'*50)
        print ('Alumnos:')
        for aula in self.escuela.aulas:
            print ('')
            aula.listar_alumnos()
            print ('')
        return False
    
    def listar_aprobados(self):
        print ('')
        print ('*'*50)
        print ('Alumnos aprobados:')
        self.escuela.listar_aprobados()
        return False
    
    def listar_alumnos_mayores_edad(self):
        print ('')
        print ('*'*50)
        print ('Alumnos mayores de edad:')
        self.escuela.listar_alumnos_mayores_edad()
        return False

    def calificar_alumnos(self, nombre_aula = None):
        print ('')
        print ('*'*50)
        print ('Calificación de Alumnos:')
        print ('')
        if nombre_aula is None:
            print('Aulas disponibles:')
            print ('')
            for aula in self.escuela.aulas:
                print(aula.nombre)
            aula = input('Nombre del aula: ')
            print ('')
            encontrado = False
            for aula in self.escuela.aulas:
                if aula.nombre == aula:
                    encontrado = True
                    aula.listar_alumnos()
                    print ('')
                    alumno = input('Nombre del alumno a calificar: ')
                    calificacion = float(input('Calificación: '))
                    if aula.calificar_alumno(alumno, calificacion):
                        print(f'Alumno {alumno} calificado correctamente en aula {aula.nombre} con una calificación de {calificacion}')
                    else:
                        print(f'Alumno {alumno} no encontrado. Calificación no realizada')
                    return False
            if encontrado == False:
                print(f'Aula {aula} no encontrada. Calificación no realizada')
                return False
        else:
                for aula in self.escuela.aulas:
                    if aula.nombre == nombre_aula:
                        aula.listar_alumnos()
                    print ('')
                    alumno = input('Nombre del alumno a calificar: ')
                    calificacion = float(input('Calificación: '))
                    if aula.calificar_alumno(alumno, calificacion):
                        print(f'Alumno {alumno} calificado correctamente en aula {aula.nombre} con una calificación de {calificacion}')
                        return False
                else:
                    print(f'Alumno {alumno} no encontrado. Calificación no realizada')
                return False


