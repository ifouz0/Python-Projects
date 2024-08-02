"""
Module Name: script
Module Description: Main Module or Script
"""
from datetime import date, time

from math import pi
from math import sqrt
from math import pow

from pylib.entities import geography
from pylib.entities import geometry
from pylib.entities import planning
from pylib.entities.planning import Event
from pylib.entities import staff
from pylib.utilities import convertutils
from pylib.utilities import mathutils
from pylib.utilities import strutils
from pylib.utilities import sysutils


def main():
    """Python DocString: Main Function or Method"""

    
    print("-" * 150)
    print("Module: math")
    print("-" * 150)
    print(f"pi: {pi}")
    print("-" * 150)

    print("-" * 150)
    print("Module: mathutils")
    print("-" * 150)
    print(f"PI: {mathutils.PI}")
    print(f"E: {mathutils.E}")
    print(f"PHI: {mathutils.PHI}")
    print(f"BASE_BINARY: {mathutils.BASE_BINARY}")
    print(f"BASE_OCTAL: {mathutils.BASE_OCTAL}")
    print(f"BASE_DECIMAL: {mathutils.BASE_DECIMAL}")
    print(f"BASE_HEXADECIMAL: {mathutils.BASE_HEXADECIMAL}")
    print(f"abs(-5): {mathutils.abs(value = -5)}")
    print(f"abs(5): {mathutils.abs(value = 5)}")
    print(f"factorial(10): {mathutils.factorial(value = 10)}")
    print(f"factorial(15): {mathutils.factorial(value = 15)}")
    for num in range(1,100):
        print(f"is_prime({num}): {mathutils.is_prime(value = num)}")
    
    print("-" * 150)

    print("-" * 150)
    print("Module: strutils")
    print("-" * 150)
    print(f"DEGREES: {strutils.DEGREES}")
    print(f"DEGREES_CELSIUS: {strutils.DEGREES_CELSIUS}")
    print(f"DEGREES_FAHRENHEIT: {strutils.DEGREES_FAHRENHEIT}")
    print(f"PRIME: {strutils.PRIME}")
    print(f"DOUBLE_PRIME: {strutils.DOUBLE_PRIME}")
    print(f"HAPPY_FACES: {strutils.HAPPY_FACE}")

    print(f"Demo: {strutils.abbreviate('Lorem ipsum bla bla car', 10)}")
    print(f"Demo: {strutils.abbreviate(text='Lorem ipsum bla bla car', max_length=10)}")
    print(f"Demo: {strutils.abbreviate(text='Lorem ipsum bla bla car', max_length=25)}")
    print(f"Demo: {strutils.abbreviate(text='Lorem ipsum bla bla car', max_length=10, placeholder='___')}")
    
    print("-" * 150)

    print("Creating random codes...")
    for i in range(10):
        print(strutils.random_code())

    print("-" * 150)

    for i in range(10):
        print(strutils.random_code_v2(length=15, uppercase_letters=True, lowercase_letters=True, digits=True,punctuation=False))

    print("-" * 150)

    codes = strutils.random_codes_v2(num_codes = 100, length = 12)
    print(f"Type: {type(codes)}")
    print(f"First code: {codes[0]}")
    print(f"Last code: {codes[-1]}")
    print("-" * 150)
    for code in codes:
        print(code)

    print("-" * 150)

    print("-" * 150)
    print("Module: planning")
    print("-" * 150)
    print(f"DAYS_LEAP_YEAR: {planning.DAYS_LEAP_YEAR}")
    print(F"DAYS_NO_LEAP_YEAR: {planning.DAYS_NO_LEAP_YEAR}")
    print(f"Current Year: {planning.current_year()}")
    print(f"Elapsed Days: {planning.elapsed_days()} days")
    print(f"Remaining Days: {planning.remaining_days()} days")
    print(f"Positional parameter: {planning.is_leap_year(2023)}")
    print(f"Keyword parameter: {planning.is_leap_year(year = 2023)}")
    print(f"Default parameter: {planning.is_leap_year()}")
    for year in range(1980, 2023, 1):
        print(f"The year {year} is leap? {planning.is_leap_year(year)} | Total Days: {planning.total_days(year)}")

    print(f"Next leap year: {planning.next_leap_year()}")
    print(f"Previous leap year: {planning.previous_leap_year()}")
    
    print(f"Year progress: {planning.year_progress(pretty = True)}")
    print(f"Year progress: {planning.year_progress(pretty = False)}")

    ev1 = planning.Event(name = "Sesion 11", date = date(year = 2022, month = planning.OCTOBER, day = 25), start_time = time(hour = 18, minute = 0), end_time = time(22,0))
    ev2 = planning.Event(name = "Sesion 12", date  = date(year = 2022, month = planning.OCTOBER, day = 27), start_time = time(hour = 18, minute = 0), end_time = time(22,0))
    ev3 = planning.Event(name = "Sesion 13", date = date(2022, planning.OCTOBER, 31), start_time = time(hour = 18, minute = 0), end_time = time(22,0))
    ev4 = planning.Event(name = "Festivo: Todos los Santos", date = date(day = 1, month = planning.NOVEMBER, year = 2022))
    events_list = [ev1, ev2, ev3, ev4]
    events_tuple = ev1, ev2, ev3, ev4

    for event in events_tuple:
        print("-" * 150)
        print(f"Estado: {event.__dict__}")
        print(f"Estado: {vars(event)}")
        print("-" * 150)
        print("-" * 150)
        print(f"ID: {event.id}")
        print("-" * 150)
        print(f"Name: {event.name}")
        print(f"Date: {event.date}")
        print(f"Start Time: {event.start_time}")
        print(f"End Time: {event.end_time}")
        print(f"Public: {event.public}")
        print(f"Description: {event.description}")
        print("-" * 150)
        print(f"Duración: {event.duration()}")
        print(f"Duración: {len(event)} minutes")
        print(f"Time left: {event.time_left()}")
        print("-" * 150)
    

    print("-" * 150)
    print("Module: convertutils")
    print("-" * 150)

    bmi_info = convertutils.bmi(weight = 81.5, height = 1.86)
    print(f"BMI Index: {bmi_info[0]:.2f}")
    print(f"BMI Category: {bmi_info[1]}")

    bmi_index,_,bmi_category = convertutils.bmi(weight = 105.5, height = 1.86)
    print(f"BMI Index: {bmi_index:.2f}")
    print(f"BMI Category: {bmi_category}")

    bmi_index,_,_ = convertutils.bmi(weight = 105.5, height = 1.86)
    print(f"BMI Index: {bmi_index:.2f}")

    _,_,bmi_category = convertutils.bmi(weight = 105.5, height = 1.86)
    print(f"BMI Category: {bmi_category}")
    

    print("-" * 150)
    print("Module: sysutils")
    print("-" * 150)
    python_info = sysutils.python_info()
    print(f"Python Implementation: {python_info[0]}")
    print(f"Python Version: {python_info[1]}")
    print("-" * 150)
    python_i, python_v = sysutils.python_info()
    print(f"Python Implementation: {python_i}")
    print(f"Python Version: {python_v}")
    print("-" * 150)
    machine_info = sysutils.machine_info()
    print(f"Platform Machine: {machine_info[0]}")
    print(f"Platform System: {machine_info[1]}")
    print(f"Platform Platform: {machine_info[2]}")
    print(f"Platform Version: {machine_info[3]}")
    print(f"Platform Processor: {machine_info[4]}")
    print("-" * 150)


    print("-" * 150)
    print("Module: staff")
    print("-" * 150)
    print(f"Player.DEFAULT_SALARY: {staff.Player.DEFAULT_SALARY}")
    print(f"Player.DEFAULT_PAYMENTS: {staff.Player.DEFAULT_PAYMENTS}")
    print(f"Player._counter: {staff.Player.counter()}")
    p1 = staff.Player(firstname="Jordi", lastname="Ariño", birthdate = date(year = 1980, month = 10, day = 23), height = 1.86, weight = 82)
    p2 = staff.Player(firstname="Ramon", lastname="Carles", birthdate=date(year=1978, month=1, day=13), height=1.76,  weight=70)
    p3 = staff.Player(firstname="Elisabet", lastname="Castro", birthdate=date(year=1985, month=2, day=2), height=1.96, weight=75)
    p4 = staff.Player(firstname="Enrique", lastname="Ramirez", birthdate=date(year=1999, month=3, day=1), height=1.66, weight=65, hiredate=date(2021,12,15))
    p5 = staff.Player(firstname="Jordi", lastname="Alejandro", birthdate=date(year=1995, month=3, day=10), height=1.96, weight=55, hiredate=date(2022,1,1))
    p6 = staff.PlayerVIP(firstname="Laura", lastname="Garcia", birthdate=date(year=2002, month=5, day=3), height=1.83, weight=55 , hiredate=date(1980,10,23))
    p7 = staff.PlayerVIP(firstname="Pedro", lastname="Sanchez", birthdate=date(year=1995, month=5, day=3), height=1.93, weight=85, hiredate=date(1980,10,23), commission=3_500)
    
    players_list = [p1, p2, p3, p4, p5, p6, p7] # type: list
    players_tuple = p1, p2, p3, p4, p5, p6, p7  # type: tuple
    print(F"Players: {len(players_list)}")
    print(F"Players: {players_list.__len__()}")
    for player in players_list:
        print("-" * 150)
        print(f"Code: {player.code}")
        print(f"Firstname: {player.firstname}")
        print(f"Lastname: {player.lastname}")
        print(f"Birthdate: {player.birthdate}")
        print(f"Height: {player.height} m")
        print(f"Height: {player.weight} Kg")
        print(f"Hiredate: {player.hiredate}")
        print(f"Monthly Salary: {player.monthly_salary} €")
        print(f"Payments: {player.payments}")
        if (isinstance(player, staff.PlayerVIP)): print(f"Commission: {player.commission} €")
        print("-" * 150)
        print(f"Fullname: {player.fullname()}")
        print(f"Reverse Name: {player.reverse_name()}")
        print(f"Total Salary: {player.total_salary()} €")
        print(f"BMI: {player.bmi()}")
        print(f"Age: {player.age()} years")
        print(f"Seniority: {player.seniority()} days")
        print("-" * 150)
        print(f"len(player): {len(player)}")
        print("-" * 150)

    print("-" * 150)
    print(p1)
    print(p2)
    print("-" * 150)
    print(f"Years between p1 and p2: {p1 - p2}")
    print(f"Years between p1 and p3: {p1 - p3}")
    print("-" * 150)
    print(f"p1.is_younger(p2): {p1.is_younger(p2)}")
    print(f"p1.is_older(p2): {p1.is_older(p2)}")
    print(f"p1: {p1.age()} years - {p1.birthdate}")
    print(f"p2: {p2.age()} years - {p2.birthdate}")
    print(f"p1.is_younger(p2): {p1 < p2}")
    print(f"p1.is_younger(p2): {p1 <= p2}")
    print(f"p1.is_older(p2): {p1 > p2}")
    print(f"p1.is_older(p2): {p1 >= p2}")
    print("-" * 150)


    print("-" * 150)
    print("Module: geography")
    print("-" * 150)
    print(f"Location.MAX_LATITUDE: {geography.Location.MAX_LATITUDE}")
    print(f"Location.MIN_LATITUDE: {geography.Location.MIN_LATITUDE}")
    print(f"Location.MAX_LONGITUDE: {geography.Location.MAX_LONGITUDE}")
    print(f"Location.MIN_LONGITUDE: {geography.Location.MIN_LONGITUDE}")
    bcn = geography.Location(41.38879, 2.15899)
    mad = geography.Location(latitude = 40.4165, longitude = -3.70256)
    pmi = geography.Location(latitude = 39.61362, longitude = 3.02004)
    aloc1 = geography.Location.random()
    aloc2 = geography.Location.random()
    aloc3 = geography.Location.random()
    locations_list = [bcn, mad, pmi, aloc1, aloc2, aloc3]  # type: list
    locations_tuple = bcn, mad, pmi, aloc1, aloc2, aloc3  # type: tuple
    for location in locations_list:
        print("-" * 150)
        print(f"Estado: {location.__dict__}")
        print(f"Estado: {vars(location)}")
        print("-" * 150)
        print(f"Latitude: {location.latitude}")
        print(f"Longitude: {location.longitude}")
        print("-" * 150)
        print(f"Latitude: {location.latitude_deg(decimals=3, cpoint=False)}")
        print(f"Latitude: {location.latitude_deg(decimals=3, cpoint=True)}")
        print(f"Longitude: {location.longitude_deg(decimals=3, cpoint=False)}")
        print(f"Longitude: {location.longitude_deg(decimals=3, cpoint=True)}")
        print(f"Coordinates: {location.to_degrees(decimals=4, cpoint=False)}")
        print(f"Coordinates: {location.to_degrees(decimals=4, cpoint=True)}")
        print("-" * 150)
        print(f"Latitude: {location.latitude_dms(decimals=3, cpoint=False)}")
        print(f"Latitude: {location.latitude_dms(decimals=3, cpoint=True)}")
        print(f"Longitude: {location.longitude_dms(decimals=3, cpoint=False)}")
        print(f"Longitude: {location.longitude_dms(decimals=3, cpoint=True)}")
        print(f"Coordinates: {location.to_dms(decimals=4, cpoint=False)}")
        print(f"Coordinates: {location.to_dms(decimals=4, cpoint=True)}")
        print("-" * 150)


    print(f"BCN-MAD: {bcn.distance_to(mad)} Km")
    print(f"BCN-NY: {bcn.distance_to(geography.NEW_YORK)} Km")
    
    print(f"BCN-MAD: {bcn.midpoint_to(mad).to_degrees()}")
    print(f"BCN-NY: {bcn.midpoint_to(geography.NEW_YORK).to_degrees()}")
        

    print("-" * 150)
    print("Module: geometry")
    print("-" * 150)
    print(f"Color.MAX_VALUE: {geometry.Color.MAX_VALUE}")
    print(f"Color.MIN_VALUE: {geometry.Color.MIN_VALUE}")
    c1 = geometry.Color(name ="Black", red = geometry.Color.MIN_VALUE, green = geometry.Color.MIN_VALUE, blue = geometry.Color.MIN_VALUE)
    c2 = geometry.Color(name = "White", red = geometry.Color.MAX_VALUE, green = geometry.Color.MAX_VALUE, blue = geometry.Color.MAX_VALUE)
    c3 = geometry.Color(name = "IndianRed", red = 205, green = 92, blue = 92)
    c4 = geometry.AlphaColor(name = "White Transparent", red = geometry.Color.MAX_VALUE, green = geometry.Color.MAX_VALUE, blue = geometry.Color.MAX_VALUE, alpha = 0.5)
    c5 = geometry.AlphaColor(name = "My Color", red = 125, green = 125, blue = 125, alpha = 0.75)
    ac1 = geometry.Color.random()
    ac2 = geometry.Color.random()
    ac3 = geometry.Color.random()
    ac4 = geometry.Color.from_hex("#FF00FF")
    ac5 = geometry.Color.from_hex("#AB00FF")
    colors_list = [c1, c2, c3, c4, c5, ac1, ac2, ac3, ac4, ac5]  # type: list
    colors_tuple = c1, c2, c3, c4, c5, ac1, ac2, ac3, ac4, ac5   # type: tuple
    for color in colors_list:
        print("-" * 150)
        print(f"Estado: {color.__dict__}")
        print(f"Estado: {vars(color)}")
        print("-" * 150)
        print(f"Name: {color.name}")
        print(f"Red: {color.red}")
        print(f"Green: {color.green}")
        print(f"Blue: {color.blue}")
        if (isinstance(color, geometry.AlphaColor)): print(f"Alpha: {color.alpha}")
        print("-" * 150)
        print(f"Hex: {color.to_hex()}")
        print(f"Hex: {color.to_hex(uppercase = True)}")
        print(f"Hex: {color.to_hex(uppercase = False)}")
        print("-" * 150)



    try:
        print("-" * 100)
        vce = geography.Location(2.3, 5.2)
        print("-" * 100)
    except TypeError as error:
        print(error)
    except ValueError as error:
        print(error)
    else:
        print("INFO: Ningún error al inicializar o interactuar con el objeto")
    finally:
        print("***FINALLY****")


if __name__ == "__main__":
    main()



