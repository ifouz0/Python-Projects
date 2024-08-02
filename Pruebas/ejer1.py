from datetime import datetime, timedelta
from datetime import time
import json
class Circle:
  """
  A class representing a circle.
  
  Attributes:
    __pi (float): The value of pi (approximately 3.14).
    radius (float): The radius of the circle.
  
  Methods:
    __init__(diameter): Initializes a Circle object with the given diameter.
    area(): Calculates and returns the area of the circle.
    circumference(): Calculates and returns the circumference of the circle.
  """
  __pi = 3.14  # Atributo de clase privado que representa el valor de pi
  
  def __init__(self, diameter):
    self.radius = diameter / 2  # Inicializa el radio del círculo basado en el diámetro
  
  def area(self):
    return self.__pi * self.radius ** 2  # Calcula y retorna el área del círculo
  
  def circumference(self):
    return self.__pi * 2 * self.radius  # Calcula y retorna la circunferencia del círculo
  
  
medium_pizza = Circle(12)  # Crea un círculo con diámetro 12
teaching_table = Circle(36)  # Crea un círculo con diámetro 36
round_room = Circle(11460)  # Crea un círculo con diámetro 11460

# Imprimir resultados
print(f"Medium Pizza - Area: {medium_pizza.area()}, Circumference: {medium_pizza.circumference()}")
print(f"Teaching Table - Area: {teaching_table.area()}, Circumference: {teaching_table.circumference()}")
print(f"Round Room - Area: {round_room.area()}, Circumference: {round_room.circumference()}")
print(time.strptime('30/09/1976', "%d/%m/%Y") < datetime.now())