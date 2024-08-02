'''
    Module: Clase para convertir numeros romanos en numeros enteros y viceversa.
            El número máximo es 999.
    Author: Iván Fouz
    Version: 1.0
'''
# Importaciones del módulo
from .persona import Persona
import random
# Atributos a nivel de módulo
MIM_AGE = 12


# Definición clase
class CuentaBancaria:
    #Atributos a nivel de Clase
    
    #Inicializador
    def __init__(self, persona:'Persona') ->None:
        self._saldo = 0
        self._iban = random.randint(10000000000,999999999999)
        self.persona = persona
        self._comision = 0 if persona.esJoven() else 0.25

# Propiedades

    @property
    def saldo(self) -> int|float:
        return self._saldo

    @property
    def iban(self) -> str:
        return f'{self._iban:012d}'
    
    @property
    def comision(self) -> float:
        return self._comision

    @property
    def persona(self) -> 'persona.Persona':
        return self._persona

    @persona.setter
    def persona(self, p1: 'Persona') -> None:
        if not isinstance(p1, Persona):
            raise TypeError(f'Tipo de dato erroneo: {type(p1)}')
        if p1.edad() <= MIM_AGE:
            raise ValueError(f'El dueño de la cuenta debe tener como mínimo {MIM_AGE} años. Edad: {p1.edad()}')
        self._persona = p1

# Metodos

    def ingreso(self, cantidad: int|float) -> None:
        if  not isinstance(cantidad,int) and not isinstance(cantidad,float):
            raise TypeError(f'Tipo de Cantidad Erroneo: {type(cantidad)}')
        if cantidad < 0:
            raise ValueError(f'La Cantidad ha de ser mayor a 0: {cantidad}')
        self._saldo += cantidad * (1 - self._comision)
    
    def retirada(self, cantidad: int|float) -> None:
        if  not isinstance(cantidad,int) and not isinstance(cantidad,float):
            raise TypeError(f'Tipo de Cantidad Erroneo: {type(cantidad)}')
        if cantidad < 0:
            raise ValueError(f'La Cantidad ha de ser mayor a 0: {cantidad}')
        if cantidad > self._saldo:
            raise ValueError(f'No dispone de Saldo suficiente, Saldo: {self._saldo}')
        self._saldo -= cantidad * (1 + self._comision)

    def traspaso(self, c1:'CuentaBancaria', cantidad: int|float) -> None:
        if  not isinstance(cantidad,int) and not isinstance(cantidad,float):
            raise TypeError(f'Tipo de Cantidad Erroneo: {type(cantidad)}')
        if cantidad < 0:
            raise ValueError(f'La Cantidad ha de ser mayor a 0: {cantidad}')
        if cantidad > self._saldo:
            raise ValueError(f'No dispone de Saldo suficiente, Saldo: {self._saldo}')
        self.retirada(cantidad)
        c1.ingreso(cantidad)
