"""
Module Name: pylib.entities.geography
Module Description: Geography Module
"""

from enum import Enum
import math
import random
from pylib.utilities import convertutils
from pylib.utilities import mathutils
from pylib.utilities import strutils


# ATRIBUTOS O VARIABLES GLOBALES A NIVEL DE MODULO
EARTH_RADIUS: int = 6370

class Location:
    """Python Docstring"""

    # Definición de atributos o campos estáticos (a nivel de clase)
    MAX_LATITUDE: float = 90.0
    MIN_LATITUDE: float = -MAX_LATITUDE
    MAX_LONGITUDE: float = 180.0
    MIN_LONGITUDE: float = -MAX_LONGITUDE
    _counter: int = 0
    
    
    def __init__(self, latitude: float, longitude: float):
        """Python DocString: Inicializador del objeto"""
        # []<----- Inicializar el estado de un objeto de tipo Location
        #          e indicar los atributos o campos que definen su estado
        self.latitude = latitude
        self.longitude = longitude

    def __del__(self):
        """Python DocString: Finalizador del objeto"""
        #print(f"Location > Me están borrando del memoria o heap")

    @property
    def latitude(self) -> float|int:
        return self._latitude

    @latitude.setter
    def latitude(self, value: float|int):
        if not isinstance(value, (float,int)): raise TypeError(f"Latitude: Inappropriate argument type. Type: {type(value)}")
        if not Location.MIN_LATITUDE <= value <= Location.MAX_LATITUDE: raise ValueError(f"Latitude: Inappropriate argument value. Value: {value} (Range: {Location.MIN_LATITUDE} - {Location.MAX_LATITUDE})")
        
        self._latitude = value

    @property
    def longitude(self) -> float|int:
        return self._longitude
    
    @longitude.setter
    def longitude(self, value: float|int):
        if type(value) != float and type(value) != int: raise TypeError(f"Longitude: Inappropriate argument type. Type: {type(value)}")
        if value < Location.MIN_LONGITUDE or value > Location.MAX_LONGITUDE: raise ValueError(f"Longitude: Inappropriate argument value. Value: {value} (Range: {Location.MIN_LONGITUDE} - {Location.MAX_LONGITUDE}")
        
        self._longitude = value

    def to_tuple(self) -> tuple[float,float]:
        '''Python DocString'''
        return (self.latitude, self.longitude)

    def latitude_deg(self, decimals: int = 5, cpoint: bool = True) -> str:
        '''Python Docstring'''
        return f"{self.latitude:.{decimals}f}{strutils.DEGREES}" if not cpoint else f"{abs(self.latitude):.{decimals}f}{strutils.DEGREES} {'N' if self.latitude >= 0 else 'S'}"

    def longitude_deg(self, decimals: int = 5, cpoint: bool = True) -> str:
        '''Python Docstring'''
        return f"{self.longitude:.{decimals}f}{strutils.DEGREES}" if not cpoint else f"{abs(self.longitude):.{decimals}f}{strutils.DEGREES} {'E' if self.longitude >= 0 else 'W'}"
    
    def to_degrees(self, decimals: int = 5, cpoint: bool = True) -> str:
        '''Python Docstring'''
        return f"{self.latitude_deg(decimals, cpoint)}  {self.longitude_deg(decimals, cpoint)}"
   
    def latitude_dms(self, decimals: int = 5, cpoint: bool = True) -> str:
        '''Python Docstring'''
        (degrees, minutes, seconds) = convertutils.degrees_to_dms(self.latitude)
        return f"{degrees}{strutils.DEGREES} {minutes}{strutils.PRIME} {seconds:.{decimals}f}{strutils.DOUBLE_PRIME}" if not cpoint else f"{abs(degrees)}{strutils.DEGREES} {minutes}{strutils.PRIME} {seconds:.{decimals}f}{strutils.DOUBLE_PRIME} {'N' if degrees >= 0 else 'S'}"

    def longitude_dms(self, decimals: int = 5, cpoint: bool = True) -> str:
        '''Python Docstring'''
        (degrees, minutes, seconds) = convertutils.degrees_to_dms(self.longitude)
        return f"{degrees}{strutils.DEGREES} {minutes}{strutils.PRIME} {seconds:.{decimals}f}{strutils.DOUBLE_PRIME}" if not cpoint else f"{abs(degrees)}{strutils.DEGREES} {minutes}{strutils.PRIME} {seconds:.{decimals}f}{strutils.DOUBLE_PRIME} {'E' if degrees >= 0 else 'W'}"

    def to_dms(self, decimals: int = 5, cpoint: bool = True) -> str:
        '''Python Docstring'''
        return f"{self.latitude_dms(decimals, cpoint)}  {self.longitude_dms(decimals, cpoint)}"


    def distance_to(self, other: 'Location') -> float:
        '''Harversine Formula: http://www.movable-type.co.uk/scripts/latlong.html'''
        (rlat1, rlong1, rlat2, rlong2, dlat, dlong) = Location._radians(self, other)
        a = (math.sin(dlat/2) ** 2) + math.cos(rlat1) * math.cos(rlat2) * (math.sin(dlong/2) ** 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        return EARTH_RADIUS * c

    
    def midpoint_to(self, other: 'Location') -> 'Location':
        '''Info: https://es.distance.to/'''
        (rlat1, rlong1, rlat2, rlong2, dlat, dlong) = Location._radians(self, other)
        bx = math.cos(rlat2) * math.cos(dlong)
        by = math.cos(rlat2) * math.sin(dlong)
        lat = math.degrees(math.atan2(math.sin(rlat1) + math.sin(rlat2), math.sqrt((math.cos(rlat1) + bx) ** 2 + by ** 2)))
        long = math.degrees(rlong1 + math.atan2(by, math.cos(rlat1) + bx))
        return Location(lat, long)

    def __str__(self) -> str:
        '''Python DocString'''
        return f"({self.latitude:.2f}{strutils.DEGREES}, {self.longitude:.2f}{strutils.DEGREES})"

    def __eq__(self, other: 'Location') -> bool:
        '''Python DocString'''
        return (self.latitude == other.latitude) and (self.longitude == other.longitude)

    def __ne__(self, other: 'Location') -> bool:
        '''Python DocString'''
        return (self.latitude != other.latitude) or (self.longitude != other.longitude)

    def __sub__(self, value: 'Location'):
        """Python Docstring"""
        return self.midpoint_to(value)


    # Métodos estaticos o a nivel de clase
    @classmethod
    def random(cls) -> 'Location':
        """Python DocString: Finalizador del objeto"""
        return cls(latitude = random.uniform(cls.MIN_LATITUDE, cls.MAX_LATITUDE), longitude = random.uniform(cls.MIN_LONGITUDE, cls.MAX_LONGITUDE))


    @staticmethod
    def distance_between(loc1: 'Location', loc2: 'Location') -> float:
        '''Python DocString'''
        return loc1.distance_to(loc2)

    @staticmethod
    def midpoint_between(loc1: 'Location', loc2: 'Location') -> float:
        '''Python DocString'''
        return loc1.midpoint_to(loc2)


    @staticmethod    
    def _radians(loc1: 'Location', loc2: 'Location') -> tuple[float,float,float,float,float,float]:
        rlat1 = math.radians(loc1.latitude)
        rlong1 = math.radians(loc1.longitude)
        rlat2 = math.radians(loc2.latitude)
        rlong2 = math.radians(loc2.longitude)
        dlat = (rlat2 - rlat1)
        dlong = (rlong2 - rlong1)

        return (rlat1, rlong1, rlat2, rlong2, dlat, dlong)



class CardinalPoint(Enum):
    NORTH = (1, 'N')
    SOUTH = (2, 'S')
    WEST = (3, 'W')
    EAST = (4, 'E')




NEW_YORK = Location(latitude = 40.730610, longitude = -73.935242)
BCN = Location(latitude = 41.38879, longitude = 2.15899)
MAD = Location(latitude = 40.4165, longitude = -3.70256)
PMI = Location(latitude = 39.61362, longitude = 3.02004)