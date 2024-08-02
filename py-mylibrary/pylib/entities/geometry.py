"""
Module Name: pylib.entities.geometry
Module Description: Geometry Module
"""

import random
import re
from pylib.utilities import mathutils

class Color:
    """Python DocString"""
    
    # Definición de atributos o campos estáticos (a nivel de clase)
    MAX_VALUE: int = 255
    MIN_VALUE: int = 0
    _counter: int = 0

    def __init__(self, name: str, red: int, green: int, blue: int):
        """Python DocString: Inicializador del objeto"""
        # []<----- Inicializar el estado de un objeto de tipo Color
        #          e indicar los atributos o campos que definen su estado
        self.name = name
        self.red = red
        self.green = green
        self.blue = blue

    def __del__(self):
        """Python DocString: Finalizador del objeto"""
        #print(f"({self.red}, {self.green}, {self.blue}) > Me están borrando del memoria o heap")

    
    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value: str):
        if not isinstance(value, str): raise TypeError(f"Name: Inappropriate argument type. Type: {type(value)}")
        
        self._name = value


    @property
    def red(self) -> int:
        return self._red
    
    @red.setter
    def red(self, value: int):
        if not isinstance(value, int): raise TypeError(f"Red: Inappropriate argument type. Type: {type(value)}")
        if not Color.MIN_VALUE <= value <= Color.MAX_VALUE: raise ValueError(f"Red: Inappropriate argument value. Value: {value} (Range: {Color.MIN_LATITUDE} - {Color.MAX_LATITUDE})")
        
        self._red = value

    
    @property
    def green(self) -> int:
        return self._green
    
    @green.setter
    def green(self, value: int):
        if not isinstance(value, int): raise TypeError(f"Green: Inappropriate argument type. Type: {type(value)}")
        if not Color.MIN_VALUE <= value <= Color.MAX_VALUE: raise ValueError(f"Green: Inappropriate argument value. Value: {value} (Range: {Color.MIN_LATITUDE} - {Color.MAX_LATITUDE})")
        
        self._green = value


    @property
    def blue(self) -> int:
        return self._blue
    
    @blue.setter
    def blue(self, value: int):
        if not isinstance(value, int): raise TypeError(f"Blue: Inappropriate argument type. Type: {type(value)}")
        if not Color.MIN_VALUE <= value <= Color.MAX_VALUE: raise ValueError(f"Blue: Inappropriate argument value. Value: {value} (Range: {Color.MIN_LATITUDE} - {Color.MAX_LATITUDE})")
        
        self._blue = value


    def to_tuple(self) -> tuple[str,int,int,int]:
        '''Python DocString'''
        return (self.name, self.red, self.green, self.blue)
     
    def to_hex(self, uppercase:bool = True) -> str:
        """Python Docstring"""
        return f"#{self.red:02X}{self.green:02X}{self.blue:02X}" if uppercase else f"#{self.red:02x}{self.green:02x}{self.blue:02x}"

    def to_rgb(self, uppercase: bool = True) -> str:
        '''Python DocString'''
        return f"RGB({self.red}, {self.green}, {self.blue})" if uppercase else f"rgb({self.red}, {self.green}, {self.blue})"

    

    def __str__(self) -> str:
        '''Python DocString'''
        return f"{self.name} > {self.to_hex()}"
    
    def __eq__(self, other: 'Color') -> bool:
        '''Python DocString'''
        return (self.name == other.name) and (self.red == other.red) and (self.red == other.red) and (self.green == other.green)

    def __ne__(self, other: 'Color') -> bool:
        '''Python DocString'''
        return (self.name != other.name) or (self.red != other.red) or (self.green != other.green) or (self.blue != other.blue)

    def __lt__(self, other: 'Color') -> bool:
        '''Python DocString'''
        return self.name < other.name

    def __le__(self, other: 'Color') -> bool:
        '''Python DocString'''
        return self.name <= other.name

    def __gt__(self, other: 'Color') -> bool:
        '''Python DocString'''
        return self.name > other.name

    def __ge__(self, other: 'Color') -> bool:
        '''Python DocString'''
        return self.name >= other.name

    
    # Métodos estaticos o a nivel de clase
    @classmethod
    def random(cls) -> 'Color':
        """Python DocString"""
        return cls(name = "Random Color", red = random.randint(cls.MIN_VALUE, cls.MAX_VALUE), green = random.randint(cls.MIN_VALUE, cls.MAX_VALUE), blue = random.randint(cls.MIN_VALUE, cls.MAX_VALUE))

    @classmethod
    def from_hex(cls, value: str) -> 'Color':
        """Python DocString"""
        if not isinstance(value, str): raise TypeError(f"value: Inappropriate argument type. Type: {type(value)}")
        if not re.fullmatch(pattern = "^#[0-9A-Fa-f]{6}$", string = value): raise ValueError(f"The text {value} does not represent a correct color in hexadecimal")

        return cls(name = value, red = int(value[1:3],base = mathutils.BASE_HEXADECIMAL), green = int(value[3:5], base = mathutils.BASE_HEXADECIMAL), blue = int(value[5:7],base =  mathutils.BASE_HEXADECIMAL))

class AlphaColor(Color):
    """Python DocString"""

    # Atributos o Campos Estáticos (A nivel de clase)
    MIN_ALPHA:float = 0.0
    MAX_ALPHA:float = 1.0

    # Inicializador del objecto 
    def __init__(self, name: str, red: int, green: int, blue: int, alpha: float):
        """Python DocString: Inicializador del objeto"""
        # []<----- Inicializar el estado de un objeto de tipo Color
        #          e indicar los atributos o campos que definen su estado
        super().__init__(name, red, green, blue)
        self.alpha = alpha

    @property
    def alpha(self) -> float:
        return self._alpha

    @alpha.setter    
    def alpha(self, value: float):
        if not isinstance(value, (float, int)): raise TypeError(f"Alpha: Inappropriate argument type. Type: {type(value)}")
        if not AlphaColor.MIN_ALPHA <= value <= AlphaColor.MAX_ALPHA: raise ValueError(f"Alpha: Inappropriate argument value. Value: {value} (Range: {AlphaColor.MIN_ALPHA} - {AlphaColor.MAX_ALPHA})")
        
        self._alpha = value

    def to_hex(self, uppercase:bool = True) -> str:
        """Python Docstring"""
        return f"{super().to_hex(uppercase)} - Alpha: {self.alpha:.2f}"

    

from abc import ABC, abstractmethod

class Shape(ABC):

    _counter: int = 0
    
    def __init__(self, background_color: 'Color', fore_color: 'Color'):
        Shape._counter += 1
        self.background_color = background_color
        self.fore_color = fore_color
    
    @property
    def background_color(self) -> 'Color':
        return self._background_color

    @background_color.setter
    def background_color(self, value: 'Color'):
        if not isinstance(value, Color):
            raise TypeError("The background color of a Shape must be of type Color")
        
        self._background_color = value
  
    @property
    def fore_color(self) -> 'Color':
        return self._fore_color

    @fore_color.setter
    def fore_color(self, value: 'Color'):
        if not isinstance(value, Color):
            raise TypeError("The fore color of a Shape must be of type Color")
        
        self._fore_color = value

    
    @abstractmethod
    def area(self) -> int|float:
        return

    
    def __str__(self) -> str:
        return f"Shape: {self.__class__.__name__}\nBackground Color: {self.background_color.to_hex()}\nFore Color: {self.fore_color.to_hex()}"

class Shape_2D(Shape):
    
    _counter: int = 0

    
    @abstractmethod
    def perimeter(self) -> int|float:
        return

class Shape_3D(Shape):
    
    _counter: int = 0
    
    def __init__(self, background_color: 'Color', fore_color: 'Color'):
        Shape_3D._counter += 1
        super().__init__(background_color, fore_color)
    
    @abstractmethod
    def volume() -> int|float:
        return

class Square(Shape_2D):

    _counter: int = 0
    
    def __init__(self, side: int|float, background_color: 'Color', fore_color: 'Color'):
        Square._counter += 1
        super().__init__(background_color, fore_color)
        self.side = side

    @property
    def side(self) -> int|float:
        return self._side

    @side.setter
    def side(self, value: int|float):
        if not isinstance(value, int) and not isinstance(value,float):
            raise TypeError("The side of a square must be of type int or float")
        if value <= 0:
            raise ValueError("The side of a square must be a positive value")
        
        self._side = value


    def area(self) -> float:
        return self.side * self.side

    def perimeter(self) -> float:
        return self.side * 4


    def __str__(self) -> str:
        return f"{super().__str__()}\nSide: {self.side}\nArea: {self.area()}\nPerimeter: {self.perimeter()}"
    


    """Python DocString"""
    pass
