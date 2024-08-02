'''
    Module: personas
    Author: Ivan
    Versión: 1.0
'''


from datetime import date
class Persona:
    

    def __init__(self, Nombre: str, Apellidos: str, DNI: str,FechaNacimiento: date) -> None:
        self.nombre = Nombre
        self.apellidos = Apellidos
        self.dni = DNI
        self.fecha_nacimiento = FechaNacimiento
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, Nombre: str) -> None:
        if not isinstance(Nombre,str):
            raise TypeError(f'Tipo de dato diferente a Str, {type(Nombre)}')
        if len(Nombre) > 50:
            raise ValueError(f'El tamaño del campo es demasiado elevado: {len(Nombre)}')
        self._nombre = Nombre
    
    @property
    def apellidos(self) -> str:
        return self._apellidos
    
    @apellidos.setter
    def apellidos(self, Apellidos: str) -> None:
        if not isinstance(Apellidos,str):
            raise TypeError(f'Tipo de dato diferente a Str, {type(Apellidos)}')
        if len(Apellidos) > 50:
            raise ValueError(f'El tamaño del campo es demasiado elevado: {len(Apellidos)}')
        self._apellidos = Apellidos

    @property
    def dni(self) -> str:
        return self._dni
    
    @dni.setter
    def dni(self, DNI: str) -> None:
        DIG_CONTROL = 'TRWAGMYFPDXBNJZSQVHLCKE'
        if not isinstance(DNI,str):
            raise TypeError(f'Tipo de dato diferente a Str, {type(DNI)}')
        if len(DNI) != 9:
            raise ValueError('Formato erroneo, Formato: 00000000X')
        dig_control = DNI[8]
        num_dni = DNI[:8]
        if not num_dni.isdigit():
            raise ValueError(f'Formato erroneo, Formato: 00000000X, DIN: {DNI}')
        if dig_control not in DIG_CONTROL:
            raise ValueError(f'Formato erroneo, Formato: 00000000X, DIN: {DNI}')
        self._dni = DNI

    @property
    def fecha_nacimiento(self) -> date:
        '''Python DocString'''
        return self._fecha_nacimiento
    
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, Fecha: date):
        '''Python DocString'''
        if not isinstance(Fecha,date):
            raise TypeError(f'Tipo de dato diferente a timedate.date, {type(Fecha)}')
        if Fecha > date.today():
            raise ValueError(f'La Fecha no puede ser superion a la fecha actual: {Fecha}')
        self._fecha_nacimiento = Fecha
    
    def edad(self) -> int:
        '''Python DocString'''
        return (date.today() - self.fecha_nacimiento).days // 365
    
    def esMayorEdad(self)  -> bool:
        return self.edad() >= 18
    
    def esJoven(self) -> bool:
        return self.edad() >= 12 and self.edad() <= 18