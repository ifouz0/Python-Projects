class Alumno:
    '''Clase que representa a un alumno'''
    nombre: str
    edad: int
    calificacion: int|float

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
 #Propiedades

    @property
    def nombre(self) -> str:
        return self._nombre
    
    @property
    def edad(self) -> int:
        return self._edad
    
    @property
    def calificacion(self) -> int|float:
        return self._calificacion
    

    def __str__(self):
        return f'Alumno: {self.nombre}, Edad: {self.edad}, Grado: {self.grado}'
    
    def calificar(self, grado):
        self.calificacion = grado

    def es_mayor(self):
        return self.edad >= 18
    
    def aprobo(self):
        return self.calificacion >= 5
     

class Aula:
    '''Clase que representa un aula'''
    nombre: str
    capacidad: int
    profesor: str
    alumnos: list[Alumno]
    def __init__(self, nombre, capacidad, profesor):
        self.nombre = nombre
        self.capacidad = capacidad
        self.alumnos = []
        self.profesor = profesor

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
        for alumno in self.alumnos:
            print(alumno)
    
    def listar_aprobados(self):
        for alumno in self.alumnos:
            if alumno.aprobo():
                print(alumno)
    
    def ocupacion(self):
        return len(self.alumnos) / self.capacidad * 100

    def __str__(self):
        return f'Aula: {self.numero}, Capacidad: {self.capacidad}, Alumnos: {len(self.alumnos)}'
 

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