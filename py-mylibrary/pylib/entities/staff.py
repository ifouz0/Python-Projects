"""
Module Name: pylib.entities.staff
Module Description: Staff Module 
"""

from datetime import date
from enum import Enum
from pylib.utilities import convertutils


class Gender(Enum):
    MALE = 1
    FEMALE = 2


class Player:
    """Pythod DocString"""
    
    # Definición de atributos o campos estáticos (a nivel de clase)
    DEFAULT_SALARY: float = 1_800
    DEFAULT_PAYMENTS: int = 12
    _counter: int = 0
    
    def __init__(self, firstname: str, lastname: str, birthdate: date, height: float, weight: float, hiredate: date = date.today(), monthly_salary: float = DEFAULT_SALARY, payments: int = DEFAULT_PAYMENTS):
        """Python DocString: Inicializador del objeto"""
        # []<----- Inicializar el estado de un objeto de tipo Player
        #          e indicar los atributos o campos que definen su estado
        Player._counter += 1
        self.code = f"E{Player._counter:05d}"
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.height = height
        self.weight = weight
        self.hiredate = hiredate
        self.monthly_salary = monthly_salary
        self.payments = payments
    
    def __del__(self):
        """Python DocString: Finalizador del objeto"""
        print(f"{self.firstname} > Me están borrando del memoria o heap")

    # Comportamiento: Métodos/Operaciones a nivel de objeto
    def fullname(self) -> str:
        """Python DocString"""
        return f"{self.firstname} {self.lastname}"

    def reverse_name(self) -> str:
        """Python DocString"""
        return f"{self.lastname}, {self.firstname}"

    def bmi(self) -> tuple[float,str,str]:
        """Python DocString"""
        return convertutils.bmi(self.weight, self.height)

    def total_salary(self) -> float:
        """Python DocString"""
        return self.monthly_salary * self.payments

    def age(self) -> int:
        """Python DocString"""
        today = date.today()
        interval = today - self.birthdate
        return round(interval.days / 365.25)

    def seniority(self) -> int:
        """Python DocString"""
        today = date.today()
        interval = today - self.hiredate
        return interval.days
        
    def is_younger(self, other: 'Player') -> bool:
        """Python Docstring"""
        return self.birthdate >= other.birthdate

    def is_older(self, other: 'Player') -> bool:
        """Python Docstring"""
        return self.birthdate <= other.birthdate

    # Declaración de Magic Methods (Dunders)
    def __str__(self) -> str:
        """Python DocString: print(p1)"""
        return f"{self.code} > {self.reverse_name()} ({self.age()} years)"

    def __len__(self) -> int:
        """Python DocString: len(p1)"""
        return int(self.height * 100)

    def __sub__(self, other: 'Player') -> int :
        """Python DocString: p1 - p2"""
        return abs(self.age() - other.age())
    
    def __lt__(self, other: 'Player') -> bool:    
        """Defines behavior for the less-than operator, <"""
        return self.birthdate > other.birthdate

    def __gt__(self, other: 'Player') -> bool:
        """Defines behavior for the greater-than operator, >"""
        return self.birthdate < other.birthdate

    def __le__(self, other: 'Player') -> bool:
        """Defines behavior for the less-than-or-equal-to operator, <="""
        return self.birthdate >= other.birthdate

    def __ge__(self, other: 'Player') -> bool:
        """Defines behavior for the greater-than-or-equal-to operator, >="""
        return self.birthdate <= other.birthdate

    # Método/Operaciones estáticas
    @classmethod
    def counter(cls) -> int:
        """Python DocString"""
        return cls._counter


class PlayerVIP(Player):
    """Python DocString"""
    # Atributos o Campos Estáticos (A nivel de clase)
    DEFAULT_COMMISSION: float = 2_000

    # Inicializador del objecto 
    def __init__(self, firstname: str, lastname: str, birthdate: date, height: float, weight: float, hiredate: date = date.today(), monthly_salary: float = Player.DEFAULT_SALARY, payments: int = Player.DEFAULT_PAYMENTS, commission: float = DEFAULT_COMMISSION):
        """Python DocString: Inicializador del objeto"""
        # []<----- Inicializar el estado de un objeto de tipo Player
        #          e indicar los atributos o campos que definen su estado
        super().__init__(firstname, lastname, birthdate, height, weight, hiredate, monthly_salary, payments)
        self.commission = commission
    
    @property
    def commission(self) -> float:
        return self._commission
    @commission.setter    
    def commission(self, value: float):
        if not isinstance(value, (float, int)): raise TypeError(f"Commission: Inappropriate argument type. Type: {type(value)}")
        if value < 0: raise ValueError(f"Commission: Inappropriate argument value")
        
        self._commission = value

    # Note: Sobreescribir/Reimplementar/Redefinir un método de nuestro tipo padre (Overrides)
    def total_salary(self) -> float:
        """Python DocString"""
        return super().total_salary() + self.commission