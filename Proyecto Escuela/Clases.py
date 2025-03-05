class Alumno:
    '''Clase que representa a un alumno'''
    nombre: str
    edad: int
    calificacion: float

    def __init__(self, nombre, edad, grado=None):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    
#Metodos

    def __str__(self):
        return f'Alumno: {self.nombre}, Edad: {self.edad}, Grado: {self.grado}'
    
    def calificar(self, grado):
        self.calificacion = round(self.calificacion, 2)




    def es_mayor(self):
        return self.edad >= 18
    
    def aprobo(self):
        return self.calificacion >= 5
     

class Aula:
    '''Clase que representa un aula'''
    nombre: str
    capacidad: int
    profesor: str
    alumnos: list

    def __init__(self, nom, cap, profe):
        self.nombre = nom
        self.capacidad = cap
        self.profesor = profe
        self.alumnos = []

#Metodos

    def agregar_alumno(self, alumno):
        if len(self.alumnos) < self.capacidad:
            self.alumnos.append(alumno)
        else:
            print("El aula está llena")
    
    def eliminar_alumno(self, nombre):
        encontrado = False
        for i, alumno in enumerate(self.alumnos):
            if alumno.nombre == nombre:
                self.alumnos.pop(i)
                encontrado = True
                break
        print(f'Alumno {nombre} no encontrado') if encontrado == False else print(f'Alumno {nombre} eliminado')
    
    def buscar_alumno(self, nombre):
        for alumno in self.alumnos:
            if alumno.nombre == nombre:
                return alumno
        return None
    
    def listar_alumnos(self):
        print(f'Alumnos en el aula {self.nombre}:')
        for alumno in self.alumnos:
            print("Nombre: ", alumno.nombre)
            print("Edad: ", alumno.edad)
            print("Grado: ", alumno.grado)

    def num_alumnos(self):
        return len(self.alumnos)
    
    def listar_aprobados(self):
        for alumno in self.alumnos:
            if alumno.aprobo():
                print(alumno)
    
    def ocupacion(self):
        return len(self.alumnos) / self.capacidad * 100
    
    def calificar_alumno(self, nombre, grado):
        alumno = self.buscar_alumno(nombre)
        if alumno != None:
            alumno.calificar(grado)
            print(f'Alumno {nombre} calificado correctamente')
            return True
        else:
            print(f'Alumno {nombre} no encontrado')
            return False

    def __str__(self):
        return f'Aula: {self.numero}, Capacidad: {str(self.capacidad)}, Alumnos: {len(self.alumnos)}'
 

class Escuela:
    def __init__(self, nombre, direccion, telefono, director):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.director = director
        self.aulas = []

    def agregar_aula(self, aula):
        self.aulas.append(aula)

    def __str__(self):
        return f'Escuela: {self.nombre}, Aulas: {len(self.aulas)}'
    
    def listar_profesores_num_alumnos(self):
        profesores = {}
        for aula in self.aulas:
            if aula.profesor in profesores:
                profesores[aula.profesor] += aula.num_alumnos()
            else:
                profesores[aula.profesor] = aula.num_alumnos()
        print("Profesores y número de alumnos:")
        for profesor, num_alumnos in profesores.items():
            print(f'{profesor}: {num_alumnos}')
    
    def listar_aprobados(self):
        print("Alumnos aprobados:")
        for aula in self.aulas:
            aula.listar_aprobados()
    def listar_ocupacion(self):
        for aula in self.aulas:
            print(f'Ocupación del aula {aula.nombre}: {aula.ocupacion():,.2f} %')
    
    def listar_datos_escuela(self):
        print(f'Escuela: {self.nombre}')
        print(f'Dirección: {self.direccion}')
        print(f'Teléfono: {self.telefono}')
        print(f'Director: {self.director}')
        print(f'Aulas: {len(self.aulas)}')
        print(" Nombre de las aulas y capacidad de alumnos:")
        for aula in self.aulas:
            print(f'Mombre: {aula.nombre}, Capacidad: {aula.capacidad}')

    def obtener_alumnos(self, nombre_aula):
        for aula in self.aulas:
            if aula.nombre == nombre_aula:
                aula.listar_alumnos()
                break
    
    def obtener_alumno(self, nombre_alumno):
        for aula in self.aulas:
            alumno = aula.buscar_alumno(nombre_alumno)
            if alumno != None:
                print(alumno)
                return True
        print(f'Alumno {nombre_alumno} no encontrado')
        return False

    def listar_alumnos_mayores_edad(self):
        count = 0
        for aula in self.aulas:
            for alumno in aula.alumnos():
                if alumno.es_mayor():
                    print('Calificación: ', alumno.calificacion)
                    print('Edad: ', alumno.edad)
                    print('Grado: ', alumno.grado)
                    print('Aula: ', aula.nombre)
                    count += 1
        if count == 0:
            print('No hay alumnos mayores de edad')
        else:
            print('')
            print(f'Total alumnos mayores de edad: {count}')

    def listar_alumnos_aprobados(self):
        count = 0
        for aula in self.aulas():
            for alumno in aula.alumnos():
                if alumno.aprobo():
                    print('Nombre: ', alumno.nombre)
                    print('Edad: ', alumno.edad)
                    print('Grado: ', alumno.grado)
                    print('Aula: ', aula.nombre)
                    count += 1
        if count == 0:
            print('No hay alumnos aprobados')
        else:
            print('')
            print(f'Total alumnos aprobados: {count}')
    
    def existen_aulas(self):
        return len(self.aulas) > 0
    
    def existen_alumnos(self):
        for aula in self.aulas:
            if  aula.num_alumnos() > 0:
                return True
        return False
            

