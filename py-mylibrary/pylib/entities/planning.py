"""
Module Name: pylib.entities.planning
Module Description: Calendar or Planning Module
"""

from datetime import date, time, datetime
from pylib.utilities import strutils, convertutils

# Atributos o variables a nivel de módulo
DAYS_LEAP_YEAR: int = 366
DAYS_NO_LEAP_YEAR: int = 365
JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER =  (1,2,3,4,5,6,7,8,9,10,11,12)
MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY = 1,2,3,4,5,6,7

# Funciones o métodos a nivel de módulo (Helpers / Utilities Functions)
def current_year() -> int:
    """Python DocString"""
    today = date.today()
    return today.year

def elapsed_days() -> int:
    """Python DocString"""
    today = date.today()
    first_day = today.replace(day = 1, month = JANUARY)
    #first_day = date(year = current_year(), month = JANUARY, day = 1)
    interval = today - first_day
    return interval.days + 1

def remaining_days() -> int:
    """Python DocString"""
    today = date.today()
    last_day = today.replace(day = 31, month = DECEMBER)
    #last_day = date(day = 31, month = DECEMBER, year = current_year())
    interval = last_day - today
    return interval.days

def is_leap_year(year: int = current_year()) -> bool:
    """Python DocString"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def total_days(year: int = current_year()) -> int:
    """Python DocString"""
    return DAYS_LEAP_YEAR if is_leap_year(year) else DAYS_NO_LEAP_YEAR
    
def next_leap_year(year: int = current_year()) -> int:
    """Python DocString"""
    current_year = year + 1
    while not is_leap_year(current_year):
        current_year += 1
    return current_year

def previous_leap_year(year: int = current_year()) -> int:
    """Python DocString"""
    current_year = year - 1
    while not is_leap_year(current_year):
        current_year -= 1
    return current_year

def year_progress(pretty: bool = True) -> float|str:
    """Python DocString"""
    progress = elapsed_days() / total_days()
    return  f"{progress:.2%}" if pretty else (progress * 100)


# Clases o plantillas que definen nuestro propios tipos de datos
class Event:
    """Python DocString"""
    #ATRIBUTOS O CAMPOS ESTÁTICOS (A NIVEL DE CLASE)
    NAME_MAX_LENGTH: int = 50
    MIN_DURATION: int = 30
    START_TIME: time = time(hour = 00, minute = 00, second = 00)
    END_TIME: time = time(hour = 23, minute = 59,second = 59)

    def __init__(self,  name: str, date: date, start_time: time = START_TIME, end_time: time = END_TIME, public: bool = True, description: str = strutils.EMPTY):
        """Python DocString: Object initialization"""
        # ----> []Event 1) Declarar dinamicamentos los atributos o campos
        #               2) Inicializamos los atributos o campos a los valores indicados
        self._id = strutils.random_code_v2(length = 12, uppercase_letters = True, lowercase_letters = True, digits = True, punctuation = False)
        self.name = name
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.public = public 
        self.description = description    


    @property
    def id(self) -> str:
        """Python Docstring"""
        return self._id

    @property
    def name(self) -> str:
        """Python Docstring"""
        return self._name

    @name.setter
    def name(self, value: str):
        """Python Docstring"""
        if not type(value) is str:
            raise TypeError(f"Attribute name must be of type str. You passed a {value.__class__.__name__}")

        self._name = value

    @property
    def date(self) -> date:
        """Python Docstring"""
        return self._date

    @date.setter
    def date(self, value: date):
        """Python Docstring"""
        if not type(value) is date:
            raise TypeError(f"Attribute date must be of type date. You passed a {value.__class__.__name__}")
        
        self._date = value

    @property
    def start_time(self) -> time:
        """Python Docstring"""
        return self._start_time

    @start_time.setter
    def start_time(self, value: time):
        """Python Docstring"""
        if not type(value) is time:
            raise TypeError(f"Attribute start_time must be of type time. You passed a {value.__class__.__name__}")
        
        self._start_time = value

    @property
    def end_time(self) -> time:
        """Python Docstring"""
        return self._end_time

    @end_time.setter
    def end_time(self, value: time):
        """Python Docstring"""
        if not type(value) is time:
            raise TypeError(f"Attribute end_time must be of type time. You passed a {value.__class__.__name__}")
        
        self._end_time = value

    @property
    def public(self) -> bool:
        """Python Docstring"""
        return self._public

    @public.setter
    def public(self, value: bool):
        """Python Docstring"""
        if not type(value) is bool:
            raise TypeError(f"Attribute public must be of type bool. You passed a {value.__class__.__name__}")
       
        self._public = value

    @property
    def description(self) -> str:
        """Python Docstring"""
        return self._description

    @description.setter
    def description(self, value: str):
        """Python Docstring"""
        if not type(value) is str:
            raise TypeError(f"Attribute description must be of type str. You passed a {value.__class__.__name__}")
       
        self._description = value



    def duration(self) -> tuple[int,int]:
        """Python Docstring"""
        interval = self._end_datetime() - self._start_datetime()
        _, hours, minutes = convertutils.seconds_to_dhm(interval.total_seconds())
        return (hours, minutes)


    def time_left(self) -> tuple[int,int,int]:
        """Python Docstring"""
        now = datetime.now()
        interval = self._start_datetime() - now
        (days, hours, minutes) = convertutils.seconds_to_dhm(interval.total_seconds())
        return (days, hours, minutes)

    def time_passed(self) -> tuple[int,int,int]:
        """Python Docstring"""
        now = datetime.now()
        interval = now - self._end_datetime()
        (days, hours, minutes) = convertutils.seconds_to_dhm(interval.total_seconds())
        return (days, hours, minutes)

    def upcoming(self) -> bool:
        """Python Docstring"""
        now = datetime.now()
        return now < self._end_datetime()
    
    def inprogress(self) -> bool:
        """Python Docstring"""
        now = datetime.now()
        return now >= self._start_datetime() and now <= self._end_datetime()
    
    def finished(self) -> bool:
        """Python Docstring"""
        now = datetime.now()
        return now > self._end_datetime()
  
    def is_before(self, other: 'Event') -> bool:
        """Python Docstring"""
        return self._start_datetime() < other._start_datetime()
    
    def is_after(self, other: 'Event') -> bool:
        """Python Docstring"""
        return self._start_datetime() > other._start_datetime()

    def overloaps(self, other: 'Event') -> bool:
        """Python Docstring"""
        return (self._start_datetime() >= other._start_datetime() and self._start_datetime() <= other._end_datetime()) \
               or (self._end_datetime() >= other.start_time() and self._end_datetime() <= other._end_datetime())


    def _start_datetime(self) -> datetime:
        """Python Docstring"""
        return datetime.combine(date = self.date, time = self.start_time)
    
    def _end_datetime(self) -> datetime:
        """Python Docstring"""
        return datetime.combine(date = self.date, time = self.end_time)


    def __str__(self) -> str:
        """Python Docstring"""
        return f"{self.id} > {self.name}"

    def __repr__(self) -> str:
        """Python Docstring"""
        return f"{self.id} > {self.name}"

    def __len__(self) -> int:
        """Python Docstring"""
        interval = self._end_datetime() - self._start_datetime()
        return int(interval.total_seconds()/60)

    def __sub__(self, other: 'Event') -> tuple[int,int,int]:
        """Python Docstring"""
        diff = other._start_datetime() - self._start_datetime()
        (days,hours,minutes) = convertutils.seconds_to_dhm(diff.total_seconds())
        return (days,hours,minutes)

    def __lt__(self, other: 'Event') -> bool:
        """Python Docstring"""
        return self.is_before(other)

    def __le__(self, other: 'Event') -> bool:
        """Python Docstring"""
        return self.is_before(other) or self._start_datetime() == other._start_datetime()

    def __gt__(self, other: 'Event') -> bool:
        """Python Docstring"""
        return self.is_after(other)

    def __ge__(self, other: 'Event') -> bool:
        """Python Docstring"""
        return self.is_after(other) or self._start_datetime() == other._start_datetime()